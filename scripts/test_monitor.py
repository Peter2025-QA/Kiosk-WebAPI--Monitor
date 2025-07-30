#!/usr/bin/env python3
"""
监控功能测试脚本
快速测试监控功能，不进入循环
"""

import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from datetime import datetime
from utils.api_validator import is_api_available, get_api_validator

def test_api_status():
    """测试API状态检查"""
    print("🧪 测试API状态检查...")
    
    try:
        api_validator = get_api_validator()
        status = api_validator.get_api_status()
        
        print(f"✅ API状态检查成功")
        print(f"   - 可用性: {'是' if status['is_available'] else '否'}")
        print(f"   - 基础URL: {status['base_url']}")
        print(f"   - 错误信息: {status['error_message']}")
        
        return True
    except Exception as e:
        print(f"❌ API状态检查失败: {e}")
        return False

def test_api_availability():
    """测试API可用性检查"""
    print("\n🧪 测试API可用性检查...")
    
    try:
        available = is_api_available()
        print(f"✅ API可用性检查成功: {'可用' if available else '不可用'}")
        return True
    except Exception as e:
        print(f"❌ API可用性检查失败: {e}")
        return False

def test_project_structure():
    """测试项目结构"""
    print("\n🧪 测试项目结构...")
    
    required_files = [
        "utils/api_validator.py",
        "utils/token_manager.py",
        "config/env_config.py",
        "tests/conftest.py",
        "requirements.txt"
    ]
    
    all_exist = True
    for file_path in required_files:
        full_path = os.path.join(project_root, file_path)
        if os.path.exists(full_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - 文件不存在")
            all_exist = False
    
    return all_exist

def main():
    print("🚀 API监控功能测试")
    print("=" * 50)
    print(f"📁 项目路径: {project_root}")
    print(f"⏰ 测试时间: {datetime.now()}")
    print()
    
    # 运行测试
    tests = [
        ("项目结构", test_project_structure),
        ("API状态检查", test_api_status),
        ("API可用性检查", test_api_availability)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} 测试异常: {e}")
            results.append((test_name, False))
    
    # 显示结果
    print("\n📊 测试结果:")
    print("=" * 50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 总结: {passed}/{len(results)} 个测试通过")
    
    if passed == len(results):
        print("🎉 所有测试通过！监控功能正常。")
        print("\n💡 现在可以运行完整监控:")
        print("   python scripts/monitor_api.py")
    else:
        print("⚠️  部分测试失败，请检查配置。")

if __name__ == "__main__":
    main() 