import requests
import json
from typing import Dict, Any, Optional
from utils.token_manager import get_auth_headers
from config.env_config import BASE_URL

class RequestHandler:
    """请求处理器工具类"""
    
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get(self, endpoint: str, params: Optional[Dict] = None, token: Optional[str] = None) -> requests.Response:
        """发送GET请求"""
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(token)
        response = self.session.get(url, headers=headers, params=params)
        return response
    
    def post(self, endpoint: str, data: Optional[Dict] = None, token: Optional[str] = None) -> requests.Response:
        """发送POST请求"""
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(token)
        response = self.session.post(url, headers=headers, json=data)
        return response
    
    def put(self, endpoint: str, data: Optional[Dict] = None, token: Optional[str] = None) -> requests.Response:
        """发送PUT请求"""
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(token)
        response = self.session.put(url, headers=headers, json=data)
        return response
    
    def delete(self, endpoint: str, token: Optional[str] = None) -> requests.Response:
        """发送DELETE请求"""
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(token)
        response = self.session.delete(url, headers=headers)
        return response
    
    def patch(self, endpoint: str, data: Optional[Dict] = None, token: Optional[str] = None) -> requests.Response:
        """发送PATCH请求"""
        url = f"{self.base_url}{endpoint}"
        headers = get_auth_headers(token)
        response = self.session.patch(url, headers=headers, json=data)
        return response
    
    def validate_response(self, response: requests.Response, expected_status_codes: list = None) -> bool:
        """验证响应状态码"""
        if expected_status_codes is None:
            expected_status_codes = [200, 201]
        return response.status_code in expected_status_codes
    
    def get_response_data(self, response: requests.Response) -> Dict[str, Any]:
        """获取响应数据"""
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response", "text": response.text}
    
    def log_request(self, method: str, url: str, data: Optional[Dict] = None, response: Optional[requests.Response] = None):
        """记录请求日志"""
        print(f"\n{'='*50}")
        print(f"Request: {method} {url}")
        if data:
            print(f"Data: {json.dumps(data, indent=2)}")
        if response:
            print(f"Response Status: {response.status_code}")
            try:
                print(f"Response Data: {json.dumps(response.json(), indent=2)}")
            except:
                print(f"Response Text: {response.text}")
        print(f"{'='*50}\n")

# 创建全局请求处理器实例
request_handler = RequestHandler()
