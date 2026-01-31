# Moltbook 页面选择器参考

本文件包含 ClawdChat 技能使用的 Moltbook 页面选择器，用于准确抓取页面内容。

## 首页选择器

### 统计数据
- **总 AI agents**: `#stats .agents-count`
- **总帖子数**: `#stats .posts-count`
- **总评论数**: `#stats .comments-count`

### Feed 选择器
- **New Feed**: `#new-feed .post-item`
- **Top Feed**: `#top-feed .post-item`
- **帖子标题**: `.post-title`
- **帖子内容**: `.post-content`
- **作者信息**: `.post-author`
- **发布时间**: `.post-time`
- **评论数**: `.post-comments-count`
- **点赞数**: `.post-likes-count`

## 帖子详情页选择器

### 帖子信息
- **帖子标题**: `#post-detail .title`
- **帖子内容**: `#post-detail .content`
- **作者信息**: `#post-detail .author-info`
- **发布时间**: `#post-detail .publish-time`
- **标签**: `#post-detail .tags`

### 评论区域
- **评论列表**: `#comments .comment-item`
- **评论作者**: `.comment-author`
- **评论内容**: `.comment-content`
- **评论时间**: `.comment-time`
- **评论回复**: `.comment-replies`

## 用户页面选择器

### 用户信息
- **用户名**: `#user-profile .username`
- **用户简介**: `#user-profile .bio`
- **关注数**: `#user-profile .following-count`
- **粉丝数**: `#user-profile .followers-count`
- **发布的帖子**: `#user-posts .post-item`

## 搜索页面选择器

### 搜索结果
- **结果列表**: `#search-results .result-item`
- **结果标题**: `.result-title`
- **结果内容**: `.result-content`
- **结果作者**: `.result-author`
- **结果时间**: `.result-time`

## 分页选择器

- **下一页按钮**: `.pagination .next-page`
- **当前页码**: `.pagination .current-page`
- **总页数**: `.pagination .total-pages`

## 注意事项

1. **选择器可能会变化** - Moltbook 网站可能会更新其 HTML 结构，导致选择器失效
2. **防爬虫机制** - Moltbook 可能会有防爬虫机制，需要合理控制抓取频率
3. **异步加载** - 部分内容可能通过 AJAX 异步加载，需要等待页面完全加载
4. **验证码** - 频繁访问可能会触发验证码，需要适当处理

## 维护建议

- 定期检查选择器是否有效
- 实现选择器的容错机制
- 使用多个备选选择器提高抓取成功率
- 监控抓取过程中的错误和异常
