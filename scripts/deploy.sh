#!/bin/bash

# API测试框架自动部署脚本
# 支持一键部署到各种环境

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查依赖
check_dependencies() {
    log_info "检查系统依赖..."
    
    # 检查Python
    if ! command -v python3 &> /dev/null; then
        log_error "Python3 未安装"
        exit 1
    fi
    
    # 检查Docker
    if ! command -v docker &> /dev/null; then
        log_warning "Docker 未安装，将使用本地部署"
        USE_DOCKER=false
    else
        USE_DOCKER=true
    fi
    
    # 检查Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        log_warning "Docker Compose 未安装"
        USE_DOCKER=false
    fi
    
    log_success "依赖检查完成"
}

# 安装Python依赖
install_dependencies() {
    log_info "安装Python依赖..."
    
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt
        log_success "Python依赖安装完成"
    else
        log_error "requirements.txt 文件不存在"
        exit 1
    fi
}

# 运行测试
run_tests() {
    log_info "运行API测试..."
    
    python3 -m pytest --html=test_report.html --self-contained-html -v
    
    if [ $? -eq 0 ]; then
        log_success "所有测试通过"
    else
        log_error "测试失败"
        exit 1
    fi
}

# Docker部署
deploy_with_docker() {
    log_info "使用Docker部署..."
    
    # 构建镜像
    docker build -t kiosk-api-monitor .
    
    # 启动服务
    docker-compose up -d
    
    log_success "Docker部署完成"
}

# 本地部署
deploy_locally() {
    log_info "本地部署..."
    
    # 创建必要的目录
    mkdir -p reports logs
    
    # 启动监控脚本
    nohup python3 scripts/monitor_api.py > logs/monitor.log 2>&1 &
    
    log_success "本地部署完成"
}

# 配置通知
setup_notifications() {
    log_info "配置通知设置..."
    
    # 这里可以添加各种通知配置
    # 例如：Slack、钉钉、邮件等
    
    log_success "通知配置完成"
}

# 健康检查
health_check() {
    log_info "执行健康检查..."
    
    # 检查API可用性
    python3 -c "
from utils.api_validator import is_api_available
if is_api_available():
    print('✅ API健康检查通过')
    exit(0)
else:
    print('❌ API健康检查失败')
    exit(1)
"
    
    if [ $? -eq 0 ]; then
        log_success "健康检查通过"
    else
        log_error "健康检查失败"
        exit 1
    fi
}

# 显示部署信息
show_deployment_info() {
    log_info "部署信息:"
    echo "=================================="
    echo "🌐 测试报告: http://localhost/test_report.html"
    echo "📊 监控面板: http://localhost:8080"
    echo "📝 日志文件: ./logs/monitor.log"
    echo "🔧 管理命令:"
    echo "   - 查看日志: tail -f logs/monitor.log"
    echo "   - 停止服务: docker-compose down"
    echo "   - 重启服务: docker-compose restart"
    echo "=================================="
}

# 主函数
main() {
    echo "🚀 API测试框架自动部署脚本"
    echo "================================"
    
    # 检查依赖
    check_dependencies
    
    # 安装依赖
    install_dependencies
    
    # 运行测试
    run_tests
    
    # 健康检查
    health_check
    
    # 部署
    if [ "$USE_DOCKER" = true ]; then
        deploy_with_docker
    else
        deploy_locally
    fi
    
    # 配置通知
    setup_notifications
    
    # 显示部署信息
    show_deployment_info
    
    log_success "🎉 部署完成！"
}

# 清理函数
cleanup() {
    log_info "清理资源..."
    
    if [ "$USE_DOCKER" = true ]; then
        docker-compose down
    else
        pkill -f "monitor_api.py" || true
    fi
    
    log_success "清理完成"
}

# 信号处理
trap cleanup EXIT

# 运行主函数
main "$@" 