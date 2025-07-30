# 测试脚本验证示例

## 📋 示例：手机号登录测试脚本验证说明

### 文件：`tests/login/test_login_phone.py`

#### 🎯 验证目的
手机号登录功能测试，验证用户通过手机号和验证码进行登录的功能。

#### 🔗 API目标
- **端点：** `/auth/login/phone`
- **方法：** POST
- **基础URL：** `https://staging.orderwithinfi.com/kiosk-shopping-api`

#### ✅ 验证点

| 验证项 | 示例代码 | 预期结果 |
|--------|----------|----------|
| 状态码是否为200（成功登录） | `assert response.status_code == 200` | 成功登录返回200状态码 |
| 响应中是否包含token字段 | `assert 'token' in response.json()` | 响应包含有效的认证token |
| 无效验证码处理 | `assert response.status_code in [401, 404]` | 无效验证码返回401或404 |
| 无效手机号处理 | `assert response.status_code in [401, 404]` | 无效手机号返回401或404 |
| 缺少验证码参数处理 | `assert response.status_code in [400, 404]` | 缺少参数返回400或404 |
| 缺少手机号参数处理 | `assert response.status_code in [400, 404]` | 缺少参数返回400或404 |

#### 🧪 测试场景

1. **正常登录流程**
   ```python
   payload = {
       "phone": "1234567890",
       "verificationCode": "123456"
   }
   ```

2. **错误验证码处理**
   ```python
   payload = {
       "phone": "1234567890",
       "verificationCode": "000000"
   }
   ```

3. **参数缺失处理**
   ```python
   payload = {
       "phone": "1234567890"
       # 缺少 verificationCode
   }
   ```

4. **多用户并发测试**
   ```python
   @pytest.mark.parametrize("phone,code", [
       ("1234567890", "123456"),
       ("9876543210", "654321"),
       ("5555555555", "111111")
   ])
   ```

#### 📊 测试统计
- **测试用例数：** 8个
- **参数化测试：** 3组数据
- **错误场景：** 4个
- **成功场景：** 4个

#### 🔧 技术实现
- 使用 `@pytest.mark.skip_if_api_unavailable` 装饰器
- 集成 `is_api_available()` 检查
- 支持404端点处理（API不可用时的优雅降级）
- 统一的请求方法和错误处理

#### 📝 维护说明
1. 当API端点发生变化时，更新URL
2. 当验证逻辑变化时，更新断言条件
3. 当新增测试场景时，添加相应的测试用例
4. 定期检查测试数据的有效性

---

## 📋 示例：验证码发送测试脚本验证说明

### 文件：`tests/verification/test_send_code.py`

#### 🎯 验证目的
验证码发送功能测试，验证系统向邮箱和手机号发送验证码的功能。

#### 🔗 API目标
- **邮箱验证码：** `/auth/send-code/email`
- **手机验证码：** `/auth/send-code/phone`
- **方法：** POST

#### ✅ 验证点

| 验证项 | 示例代码 | 预期结果 |
|--------|----------|----------|
| 邮箱验证码发送成功 | `assert response.status_code in [200, 201, 404]` | 发送成功返回200/201 |
| 手机验证码发送成功 | `assert response.status_code in [200, 201, 404]` | 发送成功返回200/201 |
| 无效邮箱格式处理 | `assert response.status_code in [400, 404]` | 无效格式返回400 |
| 无效手机号格式处理 | `assert response.status_code in [400, 404]` | 无效格式返回400 |
| 缺少邮箱参数处理 | `assert response.status_code in [400, 404]` | 缺少参数返回400 |
| 缺少手机号参数处理 | `assert response.status_code in [400, 404]` | 缺少参数返回400 |

#### 🧪 测试场景

1. **邮箱验证码发送**
   ```python
   payload = {
       "email": "test@example.com"
   }
   ```

2. **手机验证码发送**
   ```python
   payload = {
       "phone": "1234567890"
   }
   ```

3. **格式验证**
   ```python
   payload = {
       "email": "invalid-email"  # 无效邮箱格式
   }
   ```

4. **批量发送测试**
   ```python
   @pytest.mark.parametrize("email", [
       "test001@example.com",
       "test002@example.com",
       "test003@example.com"
   ])
   ```

#### 📊 测试统计
- **测试用例数：** 12个
- **参数化测试：** 6组数据
- **错误场景：** 4个
- **成功场景：** 8个

---

## 📋 示例：位置信息获取测试脚本验证说明

### 文件：`tests/location/test_get_location.py`

#### 🎯 验证目的
位置信息获取功能测试，验证系统获取位置基本信息和设置的功能。

#### 🔗 API目标
- **位置信息：** `/v1/location/info`
- **位置设置：** `/v1/location/settings`
- **方法：** GET

#### ✅ 验证点

| 验证项 | 示例代码 | 预期结果 |
|--------|----------|----------|
| 获取位置基本信息 | `assert response.status_code in [200, 404]` | 成功获取返回200 |
| 带参数获取位置信息 | `assert response.status_code in [200, 404]` | 成功获取返回200 |
| 获取位置设置 | `assert response.status_code in [200, 404]` | 成功获取返回200 |
| 多个位置ID测试 | `assert response.status_code in [200, 404]` | 成功获取返回200 |
| 404端点处理 | 优雅处理404响应 | 不抛出异常 |

#### 🧪 测试场景

1. **基本位置信息获取**
   ```python
   url = f"{BASE_URL}/v1/location/info"
   ```

2. **带参数的位置信息获取**
   ```python
   params = {
       "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
   }
   ```

3. **位置设置获取**
   ```python
   url = f"{BASE_URL}/v1/location/settings"
   ```

4. **多位置测试**
   ```python
   @pytest.mark.parametrize("location_id", [
       "5382410a-d2d7-4271-a29c-385a38ebbca9",
       "test-location-1",
       "test-location-2"
   ])
   ```

#### 📊 测试统计
- **测试用例数：** 6个
- **参数化测试：** 3组数据
- **错误场景：** 3个
- **成功场景：** 3个

---

## 📋 如何为其他测试脚本添加验证说明

### 1. 创建验证说明模板

```markdown
### 文件：`tests/模块名/test_文件名.py`

#### 🎯 验证目的
[描述测试脚本的主要验证目的]

#### 🔗 API目标
- **端点：** `/api/endpoint`
- **方法：** [GET/POST/PUT/DELETE]
- **基础URL：** [基础URL]

#### ✅ 验证点

| 验证项 | 示例代码 | 预期结果 |
|--------|----------|----------|
| [验证项1] | `assert response.status_code == 200` | [预期结果] |
| [验证项2] | `assert 'field' in response.json()` | [预期结果] |

#### 🧪 测试场景

1. **[场景1]**
   ```python
   [代码示例]
   ```

2. **[场景2]**
   ```python
   [代码示例]
   ```

#### 📊 测试统计
- **测试用例数：** [数量]
- **参数化测试：** [数量]
- **错误场景：** [数量]
- **成功场景：** [数量]
```

### 2. 更新文档

将验证说明添加到相应的文档文件中：
- `TEST_VALIDATION_GUIDE.md` - 详细说明
- `TEST_SCRIPTS_VALIDATION_LIST.md` - 简洁清单

### 3. 维护文档

定期更新文档以反映：
- API端点的变化
- 验证逻辑的更新
- 新增的测试场景
- 测试统计的变化

---

*示例文档版本：1.0*  
*最后更新：2024年7月29日* 