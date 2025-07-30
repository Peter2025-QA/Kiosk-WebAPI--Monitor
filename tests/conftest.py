#!/usr/bin/env python3
"""
Pytest配置文件 - 添加API可用性检查和跳过机制
"""

import pytest
from utils.api_validator import get_api_validator, is_api_available

# 全局API验证器
api_validator = get_api_validator()

@pytest.fixture(scope="session")
def api_status():
    """获取API状态信息"""
    return api_validator.get_api_status()

@pytest.fixture(scope="session") 
def api_available():
    """检查API是否可用的fixture"""
    return is_api_available()

def pytest_configure(config):
    """pytest配置"""
    # 添加自定义标记
    config.addinivalue_line(
        "markers", "api_required: 标记需要API可用的测试"
    )
    config.addinivalue_line(
        "markers", "skip_if_api_unavailable: 如果API不可用则跳过测试"
    )

def pytest_collection_modifyitems(config, items):
    """修改测试收集，根据API可用性跳过测试"""
    api_available = is_api_available()
    
    for item in items:
        # 如果API不可用，跳过标记为api_required的测试
        if not api_available and "api_required" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="API不可用"))
        
        # 如果API不可用，跳过标记为skip_if_api_unavailable的测试
        if not api_available and "skip_if_api_unavailable" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="API不可用"))

def pytest_runtest_setup(item):
    """测试运行前的设置"""
    # 检查是否有自定义标记
    if hasattr(item, 'funcargs'):
        # 如果测试需要API但API不可用，跳过测试
        if "api_required" in item.keywords and not is_api_available():
            pytest.skip("API不可用，跳过测试") 