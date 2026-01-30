# 代码审查案例：支付回调处理器 (Payment Callback Handler)

## 待审代码 (Bad Sample)

```javascript
// controllers/paymentController.js
// 问题：直接使用字符串拼接、缺少日志记录、依赖不稳定
async function handleWebhook(req, res) {
  const data = req.body;
  
  // 直接更新数据库
  const query = "UPDATE orders SET status = 'paid' WHERE id = " + data.orderId;
  await db.query(query);

  // 发送通知
  emailService.send(data.userEmail, "Payment Success");

  res.send({ success: true });
}
```

## 审查意见 (Review Comments)

### 1. 严重安全隐患 (Security)
- **❌ SQL 注入**: 变量 `data.orderId` 直接拼接到查询字符串中。必须改用参数化查询。
- **❌ 缺少验签**: Webhook 属于高敏感接口,未验证请求是否来自真实的支付网关(如 Stripe/Alipay 签名验证)。

### 2. 健壮性与鲁棒性 (Robustness)
- **❌ 缺少事务**: 如果邮件发送失败,数据库状态已修改且未回滚,会导致状态不一致。
- **❌ 幂等性缺失**: 支付网关可能发送多次相同通知。需检查订单当前状态,避免重复处理。

## 改进代码 (Good Sample)

```javascript
async function handleWebhook(req, res) {
    const sig = req.headers['stripe-signature'];
    let event;

    try {
        // 1. 验证签名 (安全)
        event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
    } catch (err) {
        logger.error(`Webhook Signature verification failed: ${err.message}`);
        return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    const orderId = event.data.object.metadata.orderId;

    // 2. 检查幂等性
    const order = await db.orders.findUnique({ where: { id: orderId } });
    if (order.status === 'paid') {
        return res.send({ received: true, message: 'Already processed' });
    }

    // 3. 执行事务更新
    await db.$transaction(async (tx) => {
        await tx.orders.update({
            where: { id: orderId },
            data: { status: 'paid' }
        });
        await tx.notifications.create({ 
            data: { userId: order.userId, type: 'PAYMENT_SUCCESS' } 
        });
    });

    res.send({ received: true });
}
```
