#!/usr/bin/env python3
"""
双语日志测试脚本
Bilingual Logging Test Script
演示中英文混合的日志展示功能
Demonstrate bilingual (Chinese & English) logging functionality
"""

import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from datetime import datetime
import logging

# 配置双语日志
def setup_bilingual_logging():
    """设置双语日志配置"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('logs/bilingual_test.log', encoding='utf-8')
        ]
    )
    return logging.getLogger(__name__)

def log_bilingual(message_cn, message_en, icon="📊"):
    """记录双语日志"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
    log_message = f"{timestamp} - INFO - {icon} {message_cn} | {message_en}"
    print(log_message)
    return log_message

def test_bilingual_logging():
    """测试双语日志功能"""
    print("🚀 双语日志测试开始 | Bilingual Logging Test Started")
    print("=" * 80)
    
    # 模拟生产环境监控日志
    test_messages = [
        ("🚀 生产环境连续监控模式 - 只在发现差异时通知", 
         "🚀 Production environment continuous monitoring mode - only notify when differences are found"),
        
        ("⏰ 检查时间范围: 1分钟", 
         "⏰ Check time range: 1 minute"),
        
        ("📋 没有找到需要对比的订单", 
         "📋 No orders found that need to be compared"),
        
        ("✅ API状态检查通过", 
         "✅ API status check passed"),
        
        ("🧪 开始运行测试套件", 
         "🧪 Starting test suite execution"),
        
        ("📊 生成监控报告", 
         "📊 Generating monitoring report"),
        
        ("📧 发送通知到管理员", 
         "📧 Sending notification to administrator"),
        
        ("🔄 监控循环继续运行", 
         "🔄 Monitoring loop continues running"),
        
        ("⚠️ 检测到异常情况", 
         "⚠️ Abnormal situation detected"),
        
        ("🎉 所有任务完成", 
         "🎉 All tasks completed")
    ]
    
    # 输出双语日志
    for message_cn, message_en in test_messages:
        log_bilingual(message_cn, message_en)
        import time
        time.sleep(0.5)  # 模拟时间间隔
    
    print("=" * 80)
    print("✅ 双语日志测试完成 | Bilingual Logging Test Completed")

def test_api_monitoring_simulation():
    """模拟API监控场景"""
    print("\n🔄 模拟API监控场景 | Simulating API Monitoring Scenario")
    print("=" * 80)
    
    # 模拟连续监控
    for i in range(3):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
        
        # 模拟检查循环
        log_bilingual(
            "🚀 生产环境连续监控模式 - 只在发现差异时通知",
            "🚀 Production environment continuous monitoring mode - only notify when differences are found"
        )
        
        log_bilingual(
            "⏰ 检查时间范围: 1分钟",
            "⏰ Check time range: 1 minute"
        )
        
        log_bilingual(
            "📋 没有找到需要对比的订单",
            "📋 No orders found that need to be compared"
        )
        
        print(f"--- 第 {i+1} 次检查完成 | Check {i+1} completed ---")
        
        if i < 2:  # 不是最后一次
            import time
            time.sleep(1)  # 等待1秒
    
    print("=" * 80)
    print("✅ API监控模拟完成 | API Monitoring Simulation Completed")

def main():
    """主函数"""
    print("🎯 双语日志演示 | Bilingual Logging Demo")
    print("=" * 80)
    
    # 测试基本双语日志
    test_bilingual_logging()
    
    # 测试API监控场景
    test_api_monitoring_simulation()
    
    print("\n📋 使用说明 | Usage Instructions:")
    print("1. 运行双语监控: python3 scripts/monitor_api_bilingual.py")
    print("2. 查看日志文件: tail -f logs/bilingual_monitor.log")
    print("3. 查看测试日志: tail -f logs/bilingual_test.log")
    
    print("\n🎉 演示完成！ | Demo completed!")

if __name__ == "__main__":
    main() 