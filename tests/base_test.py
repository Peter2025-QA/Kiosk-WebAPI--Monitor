#!/usr/bin/env python3
"""
基础测试类 - 提供通用的API测试功能
"""

import pytest
import requests
import json
from typing import Dict, Any, Optional
from config.env_config import BASE_URL
from utils.token_manager import get_auth_headers
from utils.api_validator import is_api_available

class BaseAPITest:
    """API测试基类"""
    
    @property
    def base_url(self):
        return BASE_URL
    
    @property
    def headers(self):
        return get_auth_headers()
    
    def make_request(self, method: str, endpoint: str, data: Optional[Dict] = None, 
                    headers: Optional[Dict] = None, expected_status: Optional[int] = None) -> Dict[str, Any]:
        """
        发送API请求并返回结果
        
        Args:
            method: HTTP方法 (GET, POST, PUT, DELETE)
            endpoint: API端点
            data: 请求数据
            headers: 请求头
            expected_status: 期望的状态码
            
        Returns:
            包含响应信息的字典
        """
        if not is_api_available():
            pytest.skip("API不可用")
        
        url = f"{self.base_url}{endpoint}"
        request_headers = headers or self.headers
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=request_headers, timeout=10)
            elif method.upper() == "POST":
                response = requests.post(url, headers=request_headers, json=data, timeout=10)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=request_headers, json=data, timeout=10)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=request_headers, timeout=10)
            elif method.upper() == "PATCH":
                response = requests.patch(url, headers=request_headers, json=data, timeout=10)
            else:
                raise ValueError(f"不支持的HTTP方法: {method}")
            
            # 尝试解析JSON响应
            json_data = None
            json_error = None
            try:
                json_data = response.json()
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError) as e:
                json_error = str(e)
            
            result = {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "text": response.text,
                "json": json_data,
                "json_error": json_error,
                "url": url,
                "method": method.upper()
            }
            
            # 如果指定了期望状态码，进行断言
            if expected_status is not None:
                assert response.status_code == expected_status, \
                    f"期望状态码 {expected_status}，实际状态码 {response.status_code}"
            
            return result
            
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {e}")
    
    def assert_json_response(self, response: Dict[str, Any], expected_keys: Optional[list] = None):
        """断言响应是有效的JSON格式"""
        assert response["json_error"] is None, f"JSON解析失败: {response['json_error']}"
        
        if expected_keys:
            assert response["json"] is not None, "响应不是JSON格式"
            for key in expected_keys:
                assert key in response["json"], f"响应中缺少键: {key}"
    
    def assert_error_response(self, response: Dict[str, Any], expected_error_code: Optional[str] = None):
        """断言错误响应"""
        if response["json_error"] is None and response["json"]:
            # 如果响应是JSON格式，检查错误代码
            if expected_error_code:
                assert "code" in response["json"], "响应中没有错误代码"
                assert response["json"]["code"] == expected_error_code, \
                    f"期望错误代码 {expected_error_code}，实际错误代码 {response['json']['code']}"
        else:
            # 如果响应不是JSON格式，检查状态码
            assert response["status_code"] in [400, 401, 404, 500], \
                f"期望错误状态码，实际状态码: {response['status_code']}"
    
    def skip_if_api_unavailable(self):
        """如果API不可用则跳过测试"""
        if not is_api_available():
            pytest.skip("API不可用")

@pytest.mark.api_required
class TestBaseAPI:
    """基础API测试类"""
    
    def test_api_connectivity(self):
        """测试API连接性"""
        if not is_api_available():
            pytest.skip("API不可用")
        
        url = f"{BASE_URL}/"
        headers = get_auth_headers()
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            # 即使返回404，也说明服务器是可访问的
            assert response.status_code in [200, 404], \
                f"意外的状态码: {response.status_code}"
        except requests.exceptions.RequestException as e:
            pytest.fail(f"无法连接到API服务器: {e}")
    
    def test_auth_headers(self):
        """测试认证头是否正确设置"""
        headers = get_auth_headers()
        assert "X-Realm-ID" in headers, "缺少X-Realm-ID头"
        assert "X-Appz-ID" in headers, "缺少X-Appz-ID头"
        assert headers["X-Realm-ID"] == "dev-realm", "X-Realm-ID值不正确"
        assert headers["X-Appz-ID"] == "kiosk-self-ordering", "X-Appz-ID值不正确"
    
    def test_api_validator(self):
        """测试API验证器功能"""
        from utils.api_validator import get_api_validator
        
        validator = get_api_validator()
        status = validator.get_api_status()
        
        # 验证状态信息包含必要字段
        assert "base_url" in status
        assert "is_available" in status
        assert "error_message" in status
        assert "available_endpoints" in status
        
        # 验证基础URL
        assert status["base_url"] == BASE_URL 