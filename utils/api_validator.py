#!/usr/bin/env python3
"""
API验证器 - 检查API可用性并调整测试行为
"""

import requests
import json
from typing import Dict, List, Optional, Tuple
from config.env_config import BASE_URL
from utils.token_manager import get_auth_headers

class APIValidator:
    """API验证器类"""
    
    def __init__(self):
        self.base_url = BASE_URL
        self.is_available = None
        self.available_endpoints = []
        self.error_message = ""
    
    def check_api_availability(self) -> bool:
        """检查API是否可用"""
        try:
            response = requests.get(self.base_url, timeout=10)
            self.is_available = response.status_code in [200, 404]
            if not self.is_available:
                self.error_message = f"API服务器不可用，状态码: {response.status_code}"
            return self.is_available
        except requests.exceptions.RequestException as e:
            self.is_available = False
            self.error_message = f"无法连接到API服务器: {e}"
            return False
    
    def find_working_endpoints(self) -> List[str]:
        """查找可用的端点"""
        if not self.check_api_availability():
            return []
        
        test_endpoints = [
            "/auth/login/email",
            "/auth/login/phone",
            "/api/auth/login/email", 
            "/api/auth/login/phone",
            "/v1/auth/login/email",
            "/v1/auth/login/phone",
            "/health",
            "/status",
            "/"
        ]
        
        working_endpoints = []
        
        for endpoint in test_endpoints:
            try:
                url = f"{self.base_url}{endpoint}"
                if endpoint.startswith("/auth") or endpoint.startswith("/api/auth") or endpoint.startswith("/v1/auth"):
                    response = requests.post(url, json={}, timeout=5)
                else:
                    response = requests.get(url, timeout=5)
                
                if response.status_code != 404:
                    working_endpoints.append(endpoint)
                    
            except requests.exceptions.RequestException:
                continue
        
        self.available_endpoints = working_endpoints
        return working_endpoints
    
    def get_api_status(self) -> Dict:
        """获取API状态信息"""
        status = {
            "base_url": self.base_url,
            "is_available": self.is_available,
            "error_message": self.error_message,
            "available_endpoints": self.available_endpoints
        }
        
        if self.is_available is None:
            self.check_api_availability()
            status.update({
                "is_available": self.is_available,
                "error_message": self.error_message
            })
        
        if self.is_available and not self.available_endpoints:
            self.find_working_endpoints()
            status["available_endpoints"] = self.available_endpoints
        
        return status

def get_api_validator() -> APIValidator:
    """获取API验证器实例"""
    return APIValidator()

def is_api_available() -> bool:
    """检查API是否可用的便捷函数"""
    validator = get_api_validator()
    return validator.check_api_availability()

def get_working_endpoints() -> List[str]:
    """获取可用端点的便捷函数"""
    validator = get_api_validator()
    return validator.find_working_endpoints() 