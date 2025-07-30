#!/usr/bin/env python3
"""
改进的测试运行脚本 - 包含API状态检查和详细报告
"""

import subprocess
import sys
import time
from datetime import datetime
from utils.api_validator import get_api_validator, is_api_available

def print_header(title):
    """打印标题"""
    print(f"\n{'='*60}")
    print(f"🚀 {title}")
    print(f"{'='*60}")

def print_section(title):
    """打印章节标题"""
    print(f"\n📋 {title}")
    print(f"{'-'*40}")

def check_api_status():
    """检查API状态"""
    print_section("API状态检查")
    
    validator = get_api_validator()
    status = validator.get_api_status()
    
    print(f"📡 基础URL: {status['base_url']}")
    print(f"✅ API可用性: {'是' if status['is_available'] else '否'}")
    
    if not status['is_available']:
        print(f"❌ 错误信息: {status['error_message']}")
        return False
    else:
        print(f"📋 可用端点: {len(status['available_endpoints'])}")
        if status['available_endpoints']:
            for endpoint in status['available_endpoints']:
                print(f"   - {endpoint}")
        else:
            print("   - 未找到可用的端点")
        return True

def run_tests_with_options():
    """运行测试并提供选项"""
    print_section("测试运行选项")
    
    print("请选择测试运行方式:")
    print("1. 运行所有测试")
    print("2. 运行特定模块测试")
    print("3. 运行API可用性测试")
    print("4. 生成详细报告")
    print("5. 退出")
    
    while True:
        try:
            choice = input("\n请输入选项 (1-5): ").strip()
            
            if choice == "1":
                run_all_tests()
                break
            elif choice == "2":
                run_specific_module()
                break
            elif choice == "3":
                run_api_tests()
                break
            elif choice == "4":
                generate_detailed_report()
                break
            elif choice == "5":
                print("👋 退出测试运行")
                sys.exit(0)
            else:
                print("❌ 无效选项，请重新输入")
        except KeyboardInterrupt:
            print("\n👋 用户取消操作")
            sys.exit(0)

def run_all_tests():
    """运行所有测试"""
    print_section("运行所有测试")
    
    if not is_api_available():
        print("⚠️  API不可用，将跳过需要API的测试")
        print("💡 建议先解决API连接问题")
    
    start_time = time.time()
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            "--tb=short",
            "-v",
            "--disable-warnings",
            "--color=yes"
        ], capture_output=True, text=True, timeout=600)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n⏱️  测试执行时间: {duration:.2f}秒")
        print(f"📊 退出代码: {result.returncode}")
        
        if result.stdout:
            print("\n📋 测试输出:")
            print(result.stdout)
        
        if result.stderr:
            print("\n⚠️  错误信息:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n✅ 所有测试通过!")
        else:
            print("\n❌ 部分测试失败")
            
    except subprocess.TimeoutExpired:
        print("⏰ 测试执行超时")
    except Exception as e:
        print(f"❌ 测试执行失败: {e}")

def run_specific_module():
    """运行特定模块测试"""
    print_section("运行特定模块测试")
    
    modules = [
        "tests/login",
        "tests/verification", 
        "tests/location",
        "tests/menu",
        "tests/loyalty",
        "tests/order",
        "tests/payment",
        "tests/user",
        "tests/notification"
    ]
    
    print("可用模块:")
    for i, module in enumerate(modules, 1):
        print(f"{i}. {module}")
    
    try:
        choice = input("\n请选择模块编号: ").strip()
        module_index = int(choice) - 1
        
        if 0 <= module_index < len(modules):
            selected_module = modules[module_index]
            print(f"\n🧪 运行模块: {selected_module}")
            
            result = subprocess.run([
                sys.executable, "-m", "pytest",
                selected_module,
                "--tb=short",
                "-v",
                "--disable-warnings"
            ], capture_output=True, text=True, timeout=300)
            
            print(f"📊 退出代码: {result.returncode}")
            
            if result.stdout:
                print("\n📋 测试输出:")
                print(result.stdout)
            
            if result.stderr:
                print("\n⚠️  错误信息:")
                print(result.stderr)
                
        else:
            print("❌ 无效的模块编号")
            
    except (ValueError, KeyboardInterrupt):
        print("❌ 无效输入或用户取消")

def run_api_tests():
    """运行API可用性测试"""
    print_section("API可用性测试")
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            "tests/base_test.py",
            "--tb=short",
            "-v",
            "--disable-warnings"
        ], capture_output=True, text=True, timeout=60)
        
        print(f"📊 退出代码: {result.returncode}")
        
        if result.stdout:
            print("\n📋 测试输出:")
            print(result.stdout)
        
        if result.stderr:
            print("\n⚠️  错误信息:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("⏰ 测试执行超时")
    except Exception as e:
        print(f"❌ 测试执行失败: {e}")

def generate_detailed_report():
    """生成详细报告"""
    print_section("生成详细报告")
    
    # 检查API状态
    api_available = check_api_status()
    
    # 运行测试并生成报告
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest",
            "--tb=short",
            "-v",
            "--disable-warnings",
            "--html=report.html",
            "--self-contained-html"
        ], capture_output=True, text=True, timeout=600)
        
        print(f"\n📊 测试结果:")
        print(f"退出代码: {result.returncode}")
        
        if result.stdout:
            print("\n📋 测试输出:")
            print(result.stdout)
        
        if result.stderr:
            print("\n⚠️  错误信息:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n✅ 测试完成，报告已生成")
            print("📄 HTML报告: report.html")
        else:
            print("\n❌ 部分测试失败，但报告已生成")
            
    except subprocess.TimeoutExpired:
        print("⏰ 测试执行超时")
    except Exception as e:
        print(f"❌ 测试执行失败: {e}")

def main():
    """主函数"""
    print_header("Kiosk API 测试套件 - 改进版")
    print(f"📅 运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 检查API状态
    api_available = check_api_status()
    
    if not api_available:
        print("\n⚠️  警告: API不可用")
        print("💡 建议:")
        print("   1. 检查网络连接")
        print("   2. 验证API URL配置")
        print("   3. 确认API服务器状态")
        print("   4. 联系API提供方")
        
        choice = input("\n是否继续运行测试? (y/N): ").strip().lower()
        if choice not in ['y', 'yes']:
            print("👋 退出测试运行")
            sys.exit(0)
    
    # 提供测试选项
    run_tests_with_options()

if __name__ == "__main__":
    main() 