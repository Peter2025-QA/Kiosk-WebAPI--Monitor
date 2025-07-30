#!/usr/bin/env python3
"""
Kiosk API 测试运行脚本
"""

import subprocess
import sys
import os
from typing import List, Optional

def run_pytest(tests_path: str = "tests", 
               markers: Optional[List[str]] = None,
               verbose: bool = True,
               parallel: bool = False,
               generate_report: bool = True) -> int:
    """
    运行pytest测试
    
    Args:
        tests_path: 测试路径
        markers: 测试标记列表
        verbose: 是否详细输出
        parallel: 是否并行运行
        generate_report: 是否生成报告
    
    Returns:
        退出码
    """
    
    # 构建pytest命令
    cmd = ["python", "-m", "pytest", tests_path]
    
    # 添加详细输出
    if verbose:
        cmd.append("-v")
    
    # 添加并行运行
    if parallel:
        cmd.extend(["-n", "auto"])
    
    # 添加测试标记
    if markers:
        for marker in markers:
            cmd.extend(["-m", marker])
    
    # 添加报告生成
    if generate_report:
        cmd.extend([
            "--alluredir=./allure-results",
            "--clean-alluredir"
        ])
    
    # 添加其他有用选项
    cmd.extend([
        "--tb=short",  # 简化回溯信息
        "--strict-markers",  # 严格标记检查
        "--disable-warnings",  # 禁用警告
        "--color=yes"  # 彩色输出
    ])
    
    print(f"Running command: {' '.join(cmd)}")
    
    # 运行测试
    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except Exception as e:
        print(f"Error running tests: {e}")
        return 1

def run_specific_module(module: str) -> int:
    """运行特定模块的测试"""
    return run_pytest(f"tests/{module}")

def run_specific_test(test_file: str) -> int:
    """运行特定测试文件"""
    return run_pytest(test_file)

def generate_allure_report() -> int:
    """生成Allure报告"""
    try:
        cmd = ["allure", "generate", "./allure-results", "-o", "./allure-report", "--clean"]
        print(f"Generating Allure report: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except Exception as e:
        print(f"Error generating report: {e}")
        return 1

def open_allure_report() -> int:
    """打开Allure报告"""
    try:
        cmd = ["allure", "open", "./allure-report"]
        print(f"Opening Allure report: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except Exception as e:
        print(f"Error opening report: {e}")
        return 1

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Kiosk API 测试运行器")
    parser.add_argument("--module", "-m", help="运行特定模块的测试")
    parser.add_argument("--test", "-t", help="运行特定测试文件")
    parser.add_argument("--markers", "-k", nargs="+", help="运行特定标记的测试")
    parser.add_argument("--parallel", "-p", action="store_true", help="并行运行测试")
    parser.add_argument("--no-report", action="store_true", help="不生成报告")
    parser.add_argument("--open-report", action="store_true", help="生成并打开报告")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    
    args = parser.parse_args()
    
    # 设置默认详细输出
    if not args.verbose:
        args.verbose = True
    
    # 运行测试
    if args.test:
        exit_code = run_specific_test(args.test)
    elif args.module:
        exit_code = run_specific_module(args.module)
    else:
        exit_code = run_pytest(
            markers=args.markers,
            verbose=args.verbose,
            parallel=args.parallel,
            generate_report=not args.no_report
        )
    
    # 生成报告
    if not args.no_report and exit_code == 0:
        print("\nGenerating Allure report...")
        report_exit_code = generate_allure_report()
        if report_exit_code == 0:
            print("Allure report generated successfully!")
            
            # 打开报告
            if args.open_report:
                print("Opening Allure report...")
                open_allure_report()
        else:
            print("Failed to generate Allure report!")
    
    # 打印结果
    if exit_code == 0:
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ Tests failed with exit code: {exit_code}")
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main() 