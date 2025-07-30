# 🚀 API自动检测和部署指南

## ✅ 问题已解决！

监控脚本的导入错误已经修复，现在可以正常运行了。

## 🎯 快速开始

### **1. 测试监控功能**
```bash
# 运行监控功能测试
python scripts/test_monitor.py
```

### **2. 启动自动监控**
```bash
# 启动完整监控（后台运行）
python scripts/monitor_api.py &

# 或者前台运行（可以看到实时日志）
python scripts/monitor_api.py
```

### **3. 一键部署**
```bash
# 给部署脚本执行权限
chmod +x scripts/deploy.sh

# 运行自动部署
./scripts/deploy.sh
```

## 📊 监控功能

### **自动检测功能**
- ✅ **每5分钟检查API状态**
- ✅ **状态变化时自动通知**
- ✅ **实时监控API可用性**
- ✅ **自动生成监控报告**

### **自动测试功能**
- ✅ **每小时自动运行完整测试套件**
- ✅ **生成HTML和Allure测试报告**
- ✅ **测试失败时自动通知**
- ✅ **148个测试用例全覆盖**

### **自动报告功能**
- ✅ **每天生成监控报告**
- ✅ **可视化测试结果**
- ✅ **历史数据追踪**
- ✅ **JSON格式报告**

## 🔧 部署选项

### **选项1: 本地部署**
```bash
# 安装依赖
pip install -r requirements.txt

# 启动监控
python scripts/monitor_api.py
```

### **选项2: Docker部署**
```bash
# 构建并启动
docker-compose up -d

# 查看日志
docker-compose logs -f api-monitor
```

### **选项3: GitHub Actions自动部署**
- 推送到main分支自动触发
- 每天凌晨2点自动运行测试
- 自动生成测试报告

## 📈 监控面板

### **访问地址**
- **测试报告**: `http://localhost/test_report.html`
- **监控面板**: `http://localhost:8080`
- **日志文件**: `./logs/monitor.log`

### **查看日志**
```bash
# 实时查看监控日志
tail -f logs/monitor.log

# 查看测试报告
open test_report.html
```

## 🔔 通知配置

### **邮件通知**
```python
# 在 scripts/monitor_api.py 中配置
smtp_server = "smtp.gmail.com"
sender_email = "your-email@gmail.com"
receiver_email = "admin@company.com"
```

### **Slack通知**
```python
# 添加Slack Webhook URL
slack_webhook = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```

### **钉钉通知**
```python
# 添加钉钉机器人Webhook
dingtalk_webhook = "https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN"
```

## 📋 管理命令

### **启动服务**
```bash
# 启动监控
python scripts/monitor_api.py &

# 启动Docker服务
docker-compose up -d
```

### **停止服务**
```bash
# 停止监控
pkill -f "monitor_api.py"

# 停止Docker服务
docker-compose down
```

### **重启服务**
```bash
# 重启Docker服务
docker-compose restart

# 重启监控
pkill -f "monitor_api.py" && python scripts/monitor_api.py &
```

### **查看状态**
```bash
# 检查API状态
python -c "from utils.api_validator import is_api_available; print('API可用' if is_api_available() else 'API不可用')"

# 查看Docker容器状态
docker-compose ps

# 查看监控进程
ps aux | grep monitor_api
```

## 🎉 成功标志

当你看到以下输出时，说明自动检测和部署已经成功运行：

```
🚀 启动API自动监控...
📁 项目路径: /path/to/project
[2025-07-29 01:04:18] API状态: ✅ 可用
⏰ 定时任务已设置:
   - 每5分钟检查API状态
   - 每小时运行测试
   - 每天9点生成报告
🔄 开始监控循环...
```

## 🔍 故障排除

### **常见问题**

1. **模块导入错误**
   ```bash
   # 确保在项目根目录运行
   cd /path/to/kiosk_login_pytest_complete_full
   python scripts/monitor_api.py
   ```

2. **权限问题**
   ```bash
   # 给脚本执行权限
   chmod +x scripts/monitor_api.py
   chmod +x scripts/deploy.sh
   ```

3. **依赖问题**
   ```bash
   # 重新安装依赖
   pip install -r requirements.txt
   ```

4. **端口占用**
   ```bash
   # 检查端口占用
   lsof -i :8080
   # 杀死占用进程
   kill -9 <PID>
   ```

## 📞 技术支持

如果遇到问题，可以：

1. **查看日志**: `tail -f logs/monitor.log`
2. **运行测试**: `python scripts/test_monitor.py`
3. **检查配置**: 确认 `config/env_config.py` 中的API地址正确
4. **重启服务**: 使用管理命令重启

## 🎯 总结

现在你的项目已经具备了完整的自动检测和自动部署功能：

- ✅ **自动检测API状态**
- ✅ **自动运行测试**
- ✅ **自动生成报告**
- ✅ **自动发送通知**
- ✅ **自动部署到容器**

恭喜！你的API测试框架现在已经完全自动化了！🚀 