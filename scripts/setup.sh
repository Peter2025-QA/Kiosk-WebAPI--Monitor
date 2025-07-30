#!/bin/bash

# Kiosk API Testing Framework - One-Click Setup Script for Mac
# 一键配置脚本，适用于其他Mac设备

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
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

log_step() {
    echo -e "${PURPLE}[STEP]${NC} $1"
}

# 显示欢迎信息
show_welcome() {
    echo ""
    echo "🚀 Kiosk API Testing Framework - One-Click Setup"
    echo "=================================================="
    echo "📱 适用于Mac设备的一键配置脚本"
    echo "⏰ 开始时间: $(date)"
    echo ""
}

# 检查系统要求
check_system_requirements() {
    log_step "检查系统要求..."
    
    # 检查操作系统
    if [[ "$OSTYPE" != "darwin"* ]]; then
        log_error "此脚本仅适用于macOS系统"
        exit 1
    fi
    
    # 检查Mac版本
    mac_version=$(sw_vers -productVersion)
    log_info "macOS版本: $mac_version"
    
    # 检查架构
    arch=$(uname -m)
    log_info "系统架构: $arch"
    
    log_success "系统要求检查通过"
}

# 检查并安装Homebrew
install_homebrew() {
    log_step "检查Homebrew..."
    
    if ! command -v brew &> /dev/null; then
        log_warning "Homebrew未安装，正在安装..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        # 配置Homebrew路径
        if [[ "$arch" == "arm64" ]]; then
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
            eval "$(/opt/homebrew/bin/brew shellenv)"
        else
            echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
            eval "$(/usr/local/bin/brew shellenv)"
        fi
        
        log_success "Homebrew安装完成"
    else
        log_success "Homebrew已安装"
    fi
}

# 检查并安装Python
install_python() {
    log_step "检查Python环境..."
    
    # 检查pyenv
    if ! command -v pyenv &> /dev/null; then
        log_warning "pyenv未安装，正在安装..."
        brew install pyenv
        
        # 配置pyenv
        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
        echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
        echo 'eval "$(pyenv init -)"' >> ~/.zshrc
        
        # 重新加载配置
        source ~/.zshrc
        log_success "pyenv安装完成"
    else
        log_success "pyenv已安装"
    fi
    
    # 安装Python 3.11
    if ! pyenv versions | grep -q "3.11"; then
        log_warning "Python 3.11未安装，正在安装..."
        pyenv install 3.11.9
        pyenv global 3.11.9
        log_success "Python 3.11安装完成"
    else
        log_success "Python 3.11已安装"
    fi
    
    # 验证Python版本
    python_version=$(python3 --version)
    log_info "Python版本: $python_version"
}

# 检查并安装Git
install_git() {
    log_step "检查Git..."
    
    if ! command -v git &> /dev/null; then
        log_warning "Git未安装，正在安装..."
        brew install git
        log_success "Git安装完成"
    else
        log_success "Git已安装"
    fi
    
    # 配置Git用户信息
    if ! git config --global user.name &> /dev/null; then
        log_warning "配置Git用户信息..."
        read -p "请输入你的Git用户名: " git_username
        read -p "请输入你的Git邮箱: " git_email
        git config --global user.name "$git_username"
        git config --global user.email "$git_email"
        log_success "Git配置完成"
    fi
}

# 克隆项目
clone_project() {
    log_step "克隆项目..."
    
    # 检查是否在项目目录中
    if [ -f "README.md" ] && [ -d "tests" ]; then
        log_info "已在项目目录中，跳过克隆"
        return
    fi
    
    # 选择克隆方式
    echo ""
    echo "请选择项目获取方式："
    echo "1. 从GitHub克隆 (推荐)"
    echo "2. 从本地复制"
    echo "3. 跳过 (已在项目目录中)"
    read -p "请选择 (1-3): " choice
    
    case $choice in
        1)
            log_info "从GitHub克隆项目..."
            if [ -d "Kiosk-WebAPI--Monitor" ]; then
                log_warning "项目目录已存在，正在删除..."
                rm -rf Kiosk-WebAPI--Monitor
            fi
            git clone https://github.com/Peter2025-QA/Kiosk-WebAPI--Monitor.git
            cd Kiosk-WebAPI--Monitor
            log_success "项目克隆完成"
            ;;
        2)
            log_info "请手动复制项目到当前目录"
            read -p "按回车键继续..."
            ;;
        3)
            log_info "跳过克隆步骤"
            ;;
        *)
            log_error "无效选择"
            exit 1
            ;;
    esac
}

# 安装Python依赖
install_dependencies() {
    log_step "安装Python依赖..."
    
    # 升级pip
    python3 -m pip install --upgrade pip
    
    # 安装依赖
    if [ -f "requirements.txt" ]; then
        pip3 install -r requirements.txt
        log_success "Python依赖安装完成"
    else
        log_error "requirements.txt文件不存在"
        exit 1
    fi
}

# 验证安装
verify_installation() {
    log_step "验证安装..."
    
    # 检查Python包
    python3 -c "import pytest, requests, schedule; print('✅ 核心依赖检查通过')"
    
    # 检查项目结构
    if [ -f "README.md" ] && [ -d "tests" ] && [ -d "utils" ]; then
        log_success "项目结构验证通过"
    else
        log_error "项目结构不完整"
        exit 1
    fi
    
    # 运行测试检查
    log_info "运行快速测试检查..."
    python3 scripts/test_monitor.py
}

# 配置环境
setup_environment() {
    log_step "配置环境..."
    
    # 创建必要的目录
    mkdir -p logs reports
    
    # 设置执行权限
    chmod +x scripts/*.sh
    chmod +x scripts/*.py
    
    log_success "环境配置完成"
}

# 显示使用指南
show_usage_guide() {
    echo ""
    echo "🎉 安装完成！"
    echo "=================================================="
    echo ""
    echo "📋 常用命令："
    echo ""
    echo "🔍 测试监控功能："
    echo "   python3 scripts/test_monitor.py"
    echo ""
    echo "🚀 启动自动监控："
    echo "   python3 scripts/monitor_api.py"
    echo ""
    echo "🧪 运行所有测试："
    echo "   python3 -m pytest"
    echo ""
    echo "📊 生成测试报告："
    echo "   python3 -m pytest --html=test_report.html"
    echo ""
    echo "⚡ 一键部署："
    echo "   ./scripts/deploy.sh"
    echo ""
    echo "📖 查看文档："
    echo "   open README.md"
    echo "   open AUTO_DEPLOYMENT_GUIDE.md"
    echo ""
    echo "🌐 项目地址："
    echo "   https://github.com/Peter2025-QA/Kiosk-WebAPI--Monitor"
    echo ""
    echo "📞 技术支持："
    echo "   查看 README.md 或 AUTO_DEPLOYMENT_GUIDE.md"
    echo ""
}

# 主函数
main() {
    show_welcome
    
    # 检查系统要求
    check_system_requirements
    
    # 安装基础工具
    install_homebrew
    install_python
    install_git
    
    # 获取项目
    clone_project
    
    # 安装依赖
    install_dependencies
    
    # 配置环境
    setup_environment
    
    # 验证安装
    verify_installation
    
    # 显示使用指南
    show_usage_guide
    
    log_success "🎉 一键配置完成！"
}

# 错误处理
trap 'log_error "脚本执行失败，请检查错误信息"; exit 1' ERR

# 运行主函数
main "$@" 