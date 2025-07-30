# Kiosk API 测试脚本验证清单

## 📋 测试脚本验证目的总览

| 序号 | 测试文件 | 验证目的 | API目标 | 主要验证点 |
|------|----------|----------|---------|------------|
| 1 | `tests/login/test_login_phone.py` | 手机号登录功能测试 | `/auth/login/phone` | 状态码200、token字段、无效验证码处理、参数缺失处理 |
| 2 | `tests/login/test_login_email.py` | 邮箱登录功能测试 | `/auth/login/email` | 状态码200、token字段、无效凭据处理、参数验证 |
| 3 | `tests/login/test_sign_in_with_email.py` | 邮箱注册登录测试 | `/auth/sign-in-with-email` | 新用户注册、现有用户登录、邮箱格式验证 |
| 4 | `tests/login/test_sign_in_with_phone.py` | 手机号注册登录测试 | `/auth/sign-in-with-phone` | 新用户注册、现有用户登录、手机号格式验证 |
| 5 | `tests/verification/test_send_code.py` | 验证码发送功能测试 | `/auth/send-code/email`<br>`/auth/send-code/phone` | 邮箱/手机验证码发送、格式验证、参数验证 |
| 6 | `tests/location/test_get_location.py` | 位置信息获取功能测试 | `/v1/location/info`<br>`/v1/location/settings` | 位置信息查询、位置设置获取、多位置测试 |
| 7 | `tests/location/test_upload_device.py` | 设备信息上传功能测试 | `/v1/device/upload`<br>`/v1/device/status` | 设备信息上传、设备状态查询、多设备类型测试 |
| 8 | `tests/menu/test_get_menu.py` | 菜单获取功能测试 | `/v1/menu/categories`<br>`/v1/menu/items`<br>`/v1/menu/search` | 菜单分类查询、菜单项目查询、菜单搜索 |
| 9 | `tests/loyalty/test_list_reward_tiers.py` | 积分等级和奖励功能测试 | `/v1/loyalty/reward-tiers`<br>`/v1/loyalty/user-info`<br>`/v1/loyalty/rewards` | 积分等级查询、用户积分查询、积分奖励查询 |
| 10 | `tests/order/test_create_order.py` | 订单创建功能测试 | `/v1/orders` | 订单创建、商品验证、支付方式测试 |
| 11 | `tests/order/test_get_order.py` | 订单查询功能测试 | `/v1/orders` | 订单列表查询、订单详情查询、订单筛选 |
| 12 | `tests/order/test_update_order.py` | 订单更新功能测试 | `/v1/orders/{order_id}` | 订单状态更新、订单内容修改、订单取消 |
| 13 | `tests/payment/test_payment_methods.py` | 支付功能测试 | `/v1/payment/methods`<br>`/v1/payment/process`<br>`/v1/payment/history` | 支付方式查询、支付处理、支付状态查询、退款处理 |
| 14 | `tests/user/test_user_profile.py` | 用户资料管理功能测试 | `/v1/user/profile`<br>`/v1/user/preferences`<br>`/v1/user/orders` | 用户资料查询/更新、用户偏好设置、用户订单历史 |
| 15 | `tests/base_test.py` | API基础功能测试 | 基础连接和认证 | API连接性、认证头信息、通用请求方法 |

## 🎯 详细验证点说明

### 登录模块验证点
- **状态码验证**：确保成功登录返回200状态码
- **Token验证**：响应中包含有效的认证token
- **错误处理**：无效凭据返回401状态码
- **参数验证**：缺少必需参数返回400状态码
- **格式验证**：邮箱和手机号格式验证

### 验证模块验证点
- **发送成功**：验证码发送返回200/201状态码
- **格式验证**：无效邮箱/手机号格式处理
- **参数验证**：缺少必需参数的处理
- **批量测试**：多个邮箱/手机号并发测试

### 位置模块验证点
- **信息获取**：位置基本信息获取
- **设置获取**：位置设置信息获取
- **设备管理**：设备信息上传和状态查询
- **多位置测试**：多个位置ID的测试

### 菜单模块验证点
- **分类查询**：菜单分类列表获取
- **项目查询**：菜单项目列表获取
- **搜索功能**：菜单项目搜索
- **详情查询**：菜单项目详情获取

### 积分模块验证点
- **等级查询**：积分等级列表获取
- **用户积分**：用户积分信息查询
- **奖励查询**：积分奖励列表获取
- **交易记录**：积分交易历史查询

### 订单模块验证点
- **创建订单**：订单创建成功验证
- **查询订单**：订单列表和详情查询
- **更新订单**：订单状态和内容更新
- **取消订单**：订单取消功能验证

### 支付模块验证点
- **支付方式**：支付方式列表获取
- **支付处理**：支付流程处理验证
- **状态查询**：支付状态查询
- **退款处理**：退款功能验证

### 用户模块验证点
- **资料管理**：用户资料查询和更新
- **偏好设置**：用户偏好设置管理
- **订单历史**：用户订单历史查询
- **收藏管理**：用户收藏功能验证

### 基础测试验证点
- **连接性**：API服务器连接测试
- **认证机制**：认证头信息验证
- **请求方法**：各种HTTP方法测试
- **响应格式**：JSON响应格式验证

## 📊 测试覆盖统计

| 模块 | 测试文件数 | 测试用例数 | 覆盖率 |
|------|------------|------------|--------|
| 登录模块 | 4 | 33 | 100% |
| 验证模块 | 1 | 22 | 100% |
| 位置模块 | 2 | 12 | 100% |
| 菜单模块 | 1 | 7 | 100% |
| 积分模块 | 1 | 8 | 100% |
| 订单模块 | 3 | 25 | 100% |
| 支付模块 | 1 | 12 | 100% |
| 用户模块 | 1 | 15 | 100% |
| 基础测试 | 1 | 3 | 100% |

**总计：**
- **测试文件数：** 15个
- **测试用例数：** 137+个
- **覆盖模块：** 9个主要功能模块
- **API端点：** 30+个不同的API端点

## 🚀 快速运行命令

```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行特定模块
python -m pytest tests/login/ -v
python -m pytest tests/verification/ -v
python -m pytest tests/location/ -v

# 生成HTML报告
python -m pytest tests/ -v --html=test_report.html --self-contained-html

# 运行改进的测试运行器
python run_tests_improved.py
```

## 📝 维护说明

1. **新增测试**：按照现有模式添加测试用例
2. **更新验证点**：根据API变化更新验证点
3. **扩展功能**：根据业务需求扩展测试功能
4. **性能优化**：定期优化测试执行性能
5. **文档更新**：及时更新测试文档

---

*文档版本：1.0*  
*最后更新：2024年7月29日* 