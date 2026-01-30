# 数据库设计示例 - 电商订单系统

> **场景描述**: 为电商平台设计订单管理相关的数据库表结构,包括订单、订单项、支付等

## 背景

某电商平台需要设计订单管理系统的数据库,要求:
- 支持多商品订单
- 支持多种支付方式
- 订单状态流转清晰
- 支持订单查询和统计
- 高并发场景下性能优秀

## 输入信息

**核心实体**:
1. 订单 (Order)
2. 订单项 (OrderItem)
3. 支付记录 (Payment)
4. 用户 (User)
5. 商品 (Product)

**业务规则**:
- 一个订单包含多个订单项
- 一个订单对应一条支付记录
- 支持订单取消和退款
- 需要记录订单状态变更历史

## 数据库设计方案

### 1. ER 图

```
User (用户)
  │
  │ 1:N
  ▼
Order (订单) ──────1:1──────▶ Payment (支付)
  │
  │ 1:N
  ▼
OrderItem (订单项) ──────N:1──────▶ Product (商品)
```

### 2. 表结构设计

#### 2.1 用户表 (users)

```sql
CREATE TABLE users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
    username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT '邮箱',
    phone VARCHAR(20) COMMENT '手机号',
    password_hash VARCHAR(255) NOT NULL COMMENT '密码哈希',
    status TINYINT DEFAULT 1 COMMENT '状态: 1-正常, 0-禁用',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    INDEX idx_email (email),
    INDEX idx_phone (phone),
    INDEX idx_status_created (status, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
```

#### 2.2 订单表 (orders)

```sql
CREATE TABLE orders (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '订单ID',
    order_no VARCHAR(32) NOT NULL UNIQUE COMMENT '订单号',
    user_id BIGINT UNSIGNED NOT NULL COMMENT '用户ID',
    total_amount DECIMAL(10,2) NOT NULL COMMENT '订单总金额',
    discount_amount DECIMAL(10,2) DEFAULT 0.00 COMMENT '优惠金额',
    actual_amount DECIMAL(10,2) NOT NULL COMMENT '实付金额',
    status TINYINT NOT NULL DEFAULT 0 COMMENT '订单状态: 0-待支付, 1-已支付, 2-已发货, 3-已完成, 4-已取消',
    payment_method VARCHAR(20) COMMENT '支付方式: alipay, wechat, card',
    shipping_address TEXT COMMENT '收货地址 JSON',
    remark VARCHAR(500) COMMENT '订单备注',
    paid_at TIMESTAMP NULL COMMENT '支付时间',
    shipped_at TIMESTAMP NULL COMMENT '发货时间',
    completed_at TIMESTAMP NULL COMMENT '完成时间',
    cancelled_at TIMESTAMP NULL COMMENT '取消时间',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    INDEX idx_order_no (order_no),
    INDEX idx_user_id (user_id),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at),
    INDEX idx_user_status_created (user_id, status, created_at),
    FOREIGN KEY (user_id) REFERENCES users(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单表';
```

#### 2.3 订单项表 (order_items)

```sql
CREATE TABLE order_items (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '订单项ID',
    order_id BIGINT UNSIGNED NOT NULL COMMENT '订单ID',
    product_id BIGINT UNSIGNED NOT NULL COMMENT '商品ID',
    product_name VARCHAR(200) NOT NULL COMMENT '商品名称快照',
    product_sku VARCHAR(100) COMMENT '商品SKU',
    price DECIMAL(10,2) NOT NULL COMMENT '商品单价',
    quantity INT NOT NULL COMMENT '购买数量',
    subtotal DECIMAL(10,2) NOT NULL COMMENT '小计金额',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    INDEX idx_order_id (order_id),
    INDEX idx_product_id (product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单项表';
```

#### 2.4 支付记录表 (payments)

```sql
CREATE TABLE payments (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '支付ID',
    payment_no VARCHAR(32) NOT NULL UNIQUE COMMENT '支付流水号',
    order_id BIGINT UNSIGNED NOT NULL UNIQUE COMMENT '订单ID',
    amount DECIMAL(10,2) NOT NULL COMMENT '支付金额',
    payment_method VARCHAR(20) NOT NULL COMMENT '支付方式',
    payment_channel VARCHAR(50) COMMENT '支付渠道',
    transaction_id VARCHAR(100) COMMENT '第三方交易号',
    status TINYINT NOT NULL DEFAULT 0 COMMENT '支付状态: 0-待支付, 1-支付成功, 2-支付失败, 3-已退款',
    paid_at TIMESTAMP NULL COMMENT '支付完成时间',
    refunded_at TIMESTAMP NULL COMMENT '退款时间',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    INDEX idx_payment_no (payment_no),
    INDEX idx_order_id (order_id),
    INDEX idx_transaction_id (transaction_id),
    INDEX idx_status (status),
    FOREIGN KEY (order_id) REFERENCES orders(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='支付记录表';
```

#### 2.5 商品表 (products)

```sql
CREATE TABLE products (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '商品ID',
    name VARCHAR(200) NOT NULL COMMENT '商品名称',
    sku VARCHAR(100) NOT NULL UNIQUE COMMENT '商品SKU',
    price DECIMAL(10,2) NOT NULL COMMENT '商品价格',
    stock INT NOT NULL DEFAULT 0 COMMENT '库存数量',
    status TINYINT DEFAULT 1 COMMENT '状态: 1-上架, 0-下架',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    INDEX idx_sku (sku),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='商品表';
```

### 3. 索引优化策略

#### 3.1 复合索引设计

**订单表关键索引**:
```sql
-- 用户订单查询 (最常用)
INDEX idx_user_status_created (user_id, status, created_at)

-- 覆盖查询: SELECT id, order_no, status, created_at FROM orders WHERE user_id = ? AND status = ?
```

**应用场景**:
- 用户查看"我的订单"列表
- 按状态筛选订单
- 按时间排序

#### 3.2 避免 N+1 查询

**问题场景**:
```sql
-- 不好的做法: N+1 查询
SELECT * FROM orders WHERE user_id = 123;  -- 1次
-- 然后对每个订单查询订单项
SELECT * FROM order_items WHERE order_id = ?;  -- N次
```

**优化方案**:
```sql
-- 使用 JOIN 一次查询
SELECT 
    o.*,
    oi.id as item_id,
    oi.product_name,
    oi.quantity,
    oi.subtotal
FROM orders o
LEFT JOIN order_items oi ON o.id = oi.order_id
WHERE o.user_id = 123
ORDER BY o.created_at DESC;
```

### 4. 查询优化示例

#### 4.1 订单统计查询

```sql
-- 用户订单统计 (使用索引 idx_user_status_created)
SELECT 
    status,
    COUNT(*) as order_count,
    SUM(actual_amount) as total_amount
FROM orders
WHERE user_id = 123
  AND created_at >= '2026-01-01'
GROUP BY status;
```

#### 4.2 热门商品查询

```sql
-- 最近30天热门商品 (需要订单项表索引)
SELECT 
    oi.product_id,
    p.name,
    SUM(oi.quantity) as total_sold,
    SUM(oi.subtotal) as total_revenue
FROM order_items oi
JOIN orders o ON oi.order_id = o.id
JOIN products p ON oi.product_id = p.id
WHERE o.status IN (2, 3)  -- 已发货或已完成
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY oi.product_id, p.name
ORDER BY total_sold DESC
LIMIT 10;
```

### 5. 数据库范式与反范式

#### 5.1 范式化设计

**优点**:
- 数据一致性高
- 减少数据冗余
- 便于维护

**示例**: 订单项表引用商品表,而非直接存储商品信息

#### 5.2 反范式设计 (快照)

**场景**: 订单项表存储 `product_name` 快照

**原因**:
- 商品信息可能变更 (价格、名称)
- 订单需要保留下单时的商品信息
- 避免历史订单数据不一致

```sql
-- 反范式: 存储商品名称快照
product_name VARCHAR(200) NOT NULL COMMENT '商品名称快照'
```

## 关键要点

- ✅ **主键设计**: 使用自增 BIGINT,预留足够空间
- ✅ **索引优化**: 复合索引遵循最左前缀原则
- ✅ **避免 N+1**: 使用 JOIN 减少查询次数
- ✅ **时间字段**: created_at, updated_at 标准化
- ✅ **软删除**: 使用 status 字段而非物理删除
- ✅ **数据快照**: 订单相关数据保留快照避免数据不一致
- ✅ **外键约束**: 合理使用外键保证数据完整性
- ✅ **字符集**: 使用 utf8mb4 支持 emoji

## 常见问题

### Q1: 为什么订单号单独存储而不直接用主键?
A: 主键是内部ID,订单号是业务ID,便于展示和查询,且可以包含业务含义(如日期前缀)。

### Q2: 如何处理高并发下的库存扣减?
A: 使用乐观锁或悲观锁,配合 Redis 预扣减,避免超卖。

### Q3: 订单表是否需要分表?
A: 当订单量超过千万级时,建议按时间或用户ID分表,提升查询性能。

## 参考资源

- [MySQL 索引优化最佳实践](https://dev.mysql.com/doc/)
- [数据库设计范式](https://en.wikipedia.org/wiki/Database_normalization)

---

> **注意**: 本示例基于 MySQL InnoDB 引擎,实际项目需根据业务规模和并发量调整设计。
