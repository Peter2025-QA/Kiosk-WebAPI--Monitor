# Kiosk API 测试套件

一个全面的API测试项目，用于测试Kiosk自助点餐系统的各种功能模块。

## 🚀 项目概述

本项目是一个基于Pytest的API测试套件，专门为Kiosk自助点餐系统设计。项目采用模块化设计，覆盖了系统的所有主要功能模块，包括用户认证、菜单管理、订单处理、支付系统等。

### ✨ 主要特性

- **全面的API覆盖**: 涵盖所有主要API端点
- **智能错误处理**: 自动处理API不可用的情况
- **模块化设计**: 按功能模块组织测试
- **详细的报告**: 生成HTML和Allure报告
- **参数化测试**: 支持多种测试数据
- **API状态检查**: 自动检测API可用性
- **自动检测和部署**: 支持自动监控和部署
- **一键配置**: 支持其他Mac设备快速部署
- **双语日志**: 支持中英文混合日志展示

## 🌐 双语日志功能

### 中英文混合日志展示

项目支持中英文双语日志，方便国际团队协作：

```bash
# 运行双语监控
python3 scripts/monitor_api_bilingual.py

# 测试双语日志功能
python3 scripts/test_bilingual.py
```

### 日志格式示例

```
2025-08-03 01:02:11,648 - INFO - 🚀 生产环境连续监控模式 - 只在发现差异时通知 | 🚀 Production environment continuous monitoring mode - only notify when differences are found
2025-08-03 01:02:12,152 - INFO - ⏰ 检查时间范围: 1分钟 | ⏰ Check time range: 1 minute
2025-08-03 01:02:12,658 - INFO - 📋 没有找到需要对比的订单 | 📋 No orders found that need to be compared
```

### 双语功能特性

- ✅ **中英文对照**: 每条日志同时显示中文和英文
- ✅ **图标标识**: 使用emoji图标增强可读性
- ✅ **时间戳**: 精确到毫秒的时间记录
- ✅ **日志级别**: INFO、WARNING、ERROR等
- ✅ **文件记录**: 自动保存到日志文件
- ✅ **实时显示**: 控制台实时输出

### 使用场景

- **国际团队协作**: 中英文对照便于理解
- **生产环境监控**: 清晰的状态展示
- **问题排查**: 双语描述便于定位问题
- **报告生成**: 支持中英文报告

## 🎯 一键配置 (适用于其他Mac设备)

### 快速开始

在其他Mac设备上，只需运行以下命令即可完成所有配置：

```bash
# 下载一键配置脚本
curl -fsSL https://raw.githubusercontent.com/Peter2025-QA/Kiosk-WebAPI--Monitor/main/scripts/setup.sh | bash

# 或者克隆项目后运行
git clone https://github.com/Peter2025-QA/Kiosk-WebAPI--Monitor.git
cd Kiosk-WebAPI--Monitor
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### 一键配置功能

- ✅ **自动安装Homebrew** - 包管理器
- ✅ **自动安装Python 3.11** - 使用pyenv管理
- ✅ **自动安装Git** - 版本控制
- ✅ **自动克隆项目** - 从GitHub获取
- ✅ **自动安装依赖** - Python包管理
- ✅ **自动配置环境** - 权限和目录设置
- ✅ **自动验证安装** - 运行测试检查

### 配置完成后

安装完成后，你可以直接使用以下命令：

```bash
# 测试监控功能
python3 scripts/test_monitor.py

# 启动自动监控
python3 scripts/monitor_api.py

# 运行所有测试
python3 -m pytest

# 一键部署
./scripts/deploy.sh
```

## 🎯 自动检测和部署

### 快速开始

#### 1. 测试监控功能
```bash
# 运行监控功能测试
python scripts/test_monitor.py
```

#### 2. 启动自动监控
```bash
# 启动完整监控（后台运行）
python scripts/monitor_api.py &

# 或者前台运行（可以看到实时日志）
python scripts/monitor_api.py
```

#### 3. 一键部署
```bash
# 给部署脚本执行权限
chmod +x scripts/deploy.sh

# 运行自动部署
./scripts/deploy.sh
```

### 自动检测功能
- ✅ **每5分钟检查API状态**
- ✅ **状态变化时自动通知**
- ✅ **实时监控API可用性**
- ✅ **自动生成监控报告**

### 自动测试功能
- ✅ **每小时自动运行完整测试套件**
- ✅ **生成HTML和Allure测试报告**
- ✅ **测试失败时自动通知**
- ✅ **151个测试用例全覆盖**

### 部署选项
- **本地部署**: 直接运行监控脚本
- **Docker部署**: 使用docker-compose
- **GitHub Actions**: 自动CI/CD流程

详细部署指南请参考: [AUTO_DEPLOYMENT_GUIDE.md](AUTO_DEPLOYMENT_GUIDE.md)

## 📋 测试覆盖范围

### 已覆盖的模块

- ✅ **用户认证** (`tests/login/`)
  - 邮箱登录测试
  - 手机号登录测试
  - 验证码发送测试

- ✅ **位置管理** (`tests/location/`)
  - 位置信息获取
  - 设备信息上传
  - 设备状态查询

- ✅ **菜单管理** (`tests/menu/`)
  - 菜单分类获取
  - 菜单项查询
  - 菜单搜索功能

- ✅ **会员系统** (`tests/loyalty/`)
  - 奖励等级查询
  - 用户会员信息
  - 交易记录查询

- ✅ **订单管理** (`tests/order/`)
  - 订单创建
  - 订单查询
  - 订单状态更新

- ✅ **支付系统** (`tests/payment/`)
  - 支付方式获取
  - 支付处理
  - 退款处理

- ✅ **用户管理** (`tests/user/`)
  - 用户资料管理
  - 用户偏好设置
  - 收藏夹管理

- ✅ **通知系统** (`tests/notification/`)
  - 通知获取
  - 通知状态更新

## 🛠️ 技术栈

- **Python 3.11+**
- **Pytest** - 测试框架
- **Requests** - HTTP客户端
- **Allure-pytest** - 测试报告
- **python-dotenv** - 环境变量管理

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

## ⚙️ 配置

### 环境配置

项目使用 `config/env_config.py` 进行基础配置：

```python
BASE_URL = "https://staging.orderwithinfi.com/kiosk-shopping-api"
REALM_ID = "dev-realm"
APPZ_ID = "kiosk-self-ordering"
```

### 测试配置

项目使用 `config/settings.py` 进行测试配置：

```python
class Settings:
    BASE_URL = "https://staging.orderwithinfi.com/kiosk-shopping-api"
    TEST_EMAILS = ["test001@example.com", "test002@example.com"]
    TEST_PHONES = ["1234567890", "9876543210"]
    # ... 更多配置
```

## 📚 文档

### 测试验证说明
- [详细测试验证说明文档](TEST_VALIDATION_GUIDE.md) - 包含每个测试脚本的详细验证目的、API目标、验证点等信息
- [测试脚本验证清单](TEST_SCRIPTS_VALIDATION_LIST.md) - 简洁的测试脚本验证目的总览表
- [测试脚本验证示例](TEST_SCRIPT_EXAMPLE.md) - 如何为测试脚本添加验证说明的示例和模板

## 🚀 快速开始
### 1. 基本测试运行

```bash
# 运行所有测试
python -m pytest

# 运行特定模块
python -m pytest tests/login/

# 运行特定测试文件
python -m pytest tests/login/test_login_email.py
```

### 2. 使用改进的测试运行器

```bash
# 交互式测试运行器
python run_tests_improved.py
```

### 3. 生成报告

```bash
# 生成HTML报告
python -m pytest --html=report.html --self-contained-html

# 生成Allure报告
python -m pytest --alluredir=./allure-results
allure serve ./allure-results
```

## 📊 测试结果分析

### API状态检查

项目包含智能的API状态检查机制：

- **自动检测**: 运行前自动检查API可用性
- **优雅降级**: API不可用时跳过相关测试
- **详细报告**: 提供API状态和错误信息

### 错误处理

- **JSON解析错误**: 自动处理非JSON响应
- **网络错误**: 超时和连接错误处理
- **状态码验证**: 灵活的状态码断言

## 📁 项目结构

```
kiosk_login_pytest_complete_full/
├── config/                     # 配置文件
│   ├── env_config.py          # 环境配置
│   └── settings.py            # 测试配置
├── tests/                      # 测试文件
│   ├── login/                 # 登录测试
│   ├── verification/          # 验证码测试
│   ├── location/              # 位置测试
│   ├── menu/                  # 菜单测试
│   ├── loyalty/               # 会员测试
│   ├── order/                 # 订单测试
│   ├── payment/               # 支付测试
│   ├── user/                  # 用户测试
│   ├── notification/          # 通知测试
│   ├── conftest.py            # Pytest配置
│   └── base_test.py           # 基础测试类
├── utils/                      # 工具类
│   ├── api_validator.py       # API验证器
│   ├── request_handler.py     # 请求处理器
│   └── token_manager.py       # 令牌管理
├── run_tests.py               # 测试运行脚本
├── run_tests_improved.py      # 改进的测试运行器
├── generate_test_report.py    # 报告生成器
├── requirements.txt            # 依赖文件
├── pytest.ini                # Pytest配置
└── README.md                  # 项目文档
```

## 🔧 工具和脚本

### 1. API验证器 (`utils/api_validator.py`)

提供API可用性检查和状态监控：

```python
from utils.api_validator import is_api_available, get_api_validator

# 检查API是否可用
if is_api_available():
    print("API可用")
else:
    print("API不可用")

# 获取详细状态
validator = get_api_validator()
status = validator.get_api_status()
```

### 2. 改进的测试运行器 (`run_tests_improved.py`)

提供交互式测试运行体验：

- API状态检查
- 模块化测试运行
- 详细报告生成
- 错误诊断

### 3. 基础测试类 (`tests/base_test.py`)

提供通用的API测试功能：

- 统一的请求处理
- 错误响应处理
- JSON解析错误处理
- 状态码验证

## 📈 测试统计

### 当前测试覆盖

- **总测试数**: 117个
- **模块数**: 8个
- **API端点**: 45+个
- **测试场景**: 200+个

### 测试类型分布

- **功能测试**: 80%
- **错误处理测试**: 15%
- **边界测试**: 5%

## 🐛 故障排除

### 常见问题

1. **API不可用**
   ```
   解决方案: 检查网络连接和API配置
   ```

2. **JSON解析错误**
   ```
   解决方案: 检查API响应格式
   ```

3. **测试超时**
   ```
   解决方案: 增加超时时间或检查网络
   ```

### 调试工具

1. **API诊断脚本**
   ```bash
   python generate_test_report.py
   ```

2. **详细日志**
   ```bash
   python -m pytest -v --tb=long
   ```

## 🤝 贡献指南

### 添加新测试

1. 在相应的模块目录下创建测试文件
2. 继承 `BaseAPITest` 类或使用 `@pytest.mark.skip_if_api_unavailable` 装饰器
3. 添加适当的错误处理和状态码验证
4. 更新文档

### 代码规范

- 使用清晰的测试函数名称
- 添加详细的文档字符串
- 包含适当的错误处理
- 使用参数化测试减少重复代码

## 📄 许可证

本项目采用 MIT 许可证。

## 📞 支持

如有问题或建议，请：

1. 检查项目文档
2. 运行诊断脚本
3. 查看测试报告
4. 联系项目维护者

---

**最后更新**: 2025年7月29日
**版本**: 2.0.0
**状态**: 生产就绪
