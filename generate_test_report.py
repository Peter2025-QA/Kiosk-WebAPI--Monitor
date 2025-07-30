#!/usr/bin/env python3
"""
测试报告生成器 - 分析API状态和测试结果
"""

import subprocess
import sys
from datetime import datetime
from utils.api_validator import get_api_validator

def run_api_diagnosis():
    """运行API诊断"""
    print("🔍 API诊断报告")
    print("=" * 60)
    
    validator = get_api_validator()
    status = validator.get_api_status()
    
    print(f"📡 基础URL: {status['base_url']}")
    print(f"✅ API可用性: {'是' if status['is_available'] else '否'}")
    
    if not status['is_available']:
        print(f"❌ 错误信息: {status['error_message']}")
        print("\n💡 建议:")
        print("   1. 检查网络连接")
        print("   2. 验证API URL是否正确")
        print("   3. 确认API服务器是否运行")
        print("   4. 联系API提供方确认服务状态")
        return False
    else:
        print(f"📋 可用端点: {len(status['available_endpoints'])}")
        if status['available_endpoints']:
            for endpoint in status['available_endpoints']:
                print(f"   - {endpoint}")
        else:
            print("   - 未找到可用的端点")
        
        print("\n💡 分析:")
        print("   - API服务器可访问但端点可能不正确")
        print("   - 需要验证正确的API路径")
        print("   - 可能需要更新测试中的端点路径")
        return True

def run_tests_with_analysis():
    """运行测试并分析结果"""
    print("\n🧪 运行测试套件")
    print("=" * 60)
    
    try:
        # 运行测试并捕获输出
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "--tb=short", 
            "-v",
            "--disable-warnings"
        ], capture_output=True, text=True, timeout=300)
        
        print("📊 测试执行结果:")
        print(result.stdout)
        
        if result.stderr:
            print("⚠️  错误信息:")
            print(result.stderr)
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ 测试执行超时")
        return False
    except Exception as e:
        print(f"❌ 测试执行失败: {e}")
        return False

def generate_summary_report():
    """生成总结报告"""
    print("\n📋 测试总结报告")
    print("=" * 60)
    print(f"📅 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # API诊断
    api_available = run_api_diagnosis()
    
    if not api_available:
        print("\n🚫 由于API不可用，跳过测试执行")
        print("\n📝 建议:")
        print("   1. 首先解决API连接问题")
        print("   2. 验证API配置信息")
        print("   3. 确认API服务状态")
        print("   4. 更新API URL或端点路径")
        return
    
    # 运行测试
    tests_passed = run_tests_with_analysis()
    
    print("\n🎯 总结:")
    if tests_passed:
        print("✅ 测试执行成功")
    else:
        print("❌ 测试执行失败")
    
    print("\n📝 下一步建议:")
    print("   1. 检查失败的测试用例")
    print("   2. 验证API端点路径")
    print("   3. 确认请求参数格式")
    print("   4. 检查认证信息")
    print("   5. 查看详细的错误日志")

def main():
    """主函数"""
    print("🚀 Kiosk API 测试报告生成器")
    print("=" * 60)
    
    generate_summary_report()
    
    print("\n✨ 报告生成完成")

if __name__ == "__main__":
    main() 