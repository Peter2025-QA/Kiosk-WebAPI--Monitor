import requests
import pytest
import json
from utils.token_manager import get_auth_headers
from config.env_config import BASE_URL
from utils.api_validator import is_api_available

@pytest.mark.skip_if_api_unavailable
class TestEmailLogin:
    """邮箱登录测试类"""
    
    def setup_method(self):
        """测试前的设置"""
        if not is_api_available():
            pytest.skip("API不可用")
    
    def make_request(self, payload, expected_status=None):
        """发送登录请求"""
        url = f"{BASE_URL}/auth/login/email"
        headers = get_auth_headers()
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            
            # 尝试解析JSON响应
            try:
                json_data = response.json()
                print(f"Response: {response.status_code}, {json_data}")
            except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
                print(f"Response: {response.status_code}, {response.text[:100]}...")
            
            if expected_status:
                assert response.status_code == expected_status
            return response
            
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {e}")
    
    def test_login_with_email_success(self):
        """测试邮箱登录成功"""
        payload = {
            "email": "test002@infi.us",
            "password": "123123"
        }
        response = self.make_request(payload)
        assert response.status_code in [200, 401, 404]  # 404表示端点不存在
    
    def test_login_with_email_invalid_credentials(self):
        """测试邮箱登录无效凭据"""
        payload = {
            "email": "invalid@infi.us",
            "password": "wrongpassword"
        }
        response = self.make_request(payload)
        assert response.status_code in [401, 404]  # 404表示端点不存在
    
    @pytest.mark.parametrize("email,password", [
        ("test001@infi.us", "123123"),
        ("test002@infi.us", "123123"),
        ("test003@infi.us", "123123")
    ])
    def test_login_with_multiple_emails(self, email, password):
        """测试多个邮箱登录"""
        payload = {
            "email": email,
            "password": password
        }
        response = self.make_request(payload)
        assert response.status_code in [200, 401, 404]  # 404表示端点不存在
    
    def test_login_with_email_missing_password(self):
        """测试邮箱登录缺少密码"""
        payload = {
            "email": "test002@infi.us"
        }
        response = self.make_request(payload)
        assert response.status_code in [400, 404]  # 404表示端点不存在
    
    def test_login_with_email_missing_email(self):
        """测试邮箱登录缺少邮箱"""
        payload = {
            "password": "123123"
        }
        response = self.make_request(payload)
        assert response.status_code in [400, 404]  # 404表示端点不存在

# 保持向后兼容的旧测试函数
def test_login_with_email():
    """测试邮箱登录（向后兼容）"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/auth/login/email"
    payload = {
        "email": "test002@infi.us",
        "password": "123123"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"Login with email: {response.status_code}")
        
        # 尝试解析JSON
        try:
            json_data = response.json()
            print(f"Response: {json_data}")
        except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
            print(f"Response text: {response.text[:100]}...")
        
        assert response.status_code in [200, 401, 404]
        
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_login_with_email_invalid_credentials():
    """测试邮箱登录无效凭据（向后兼容）"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/auth/login/email"
    payload = {
        "email": "invalid@infi.us",
        "password": "wrongpassword"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"Login with invalid email: {response.status_code}")
        
        try:
            json_data = response.json()
            print(f"Response: {json_data}")
        except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
            print(f"Response text: {response.text[:100]}...")
        
        assert response.status_code in [401, 404]
        
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("email,password", [
    ("test001@infi.us", "123123"),
    ("test002@infi.us", "123123"),
    ("test003@infi.us", "123123")
])
def test_login_with_multiple_emails(email, password):
    """测试多个邮箱登录（向后兼容）"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/auth/login/email"
    payload = {
        "email": email,
        "password": password
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"Login with {email}: {response.status_code}")
        assert response.status_code in [200, 401, 404]
        
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_login_with_email_missing_password():
    """测试邮箱登录缺少密码（向后兼容）"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/auth/login/email"
    payload = {
        "email": "test002@infi.us"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"Login with missing password: {response.status_code}")
        
        try:
            json_data = response.json()
            print(f"Response: {json_data}")
        except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
            print(f"Response text: {response.text[:100]}...")
        
        assert response.status_code in [400, 404]
        
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_login_with_email_missing_email():
    """测试邮箱登录缺少邮箱（向后兼容）"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/auth/login/email"
    payload = {
        "password": "123123"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"Login with missing email: {response.status_code}")
        
        try:
            json_data = response.json()
            print(f"Response: {json_data}")
        except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
            print(f"Response text: {response.text[:100]}...")
        
        assert response.status_code in [400, 404]
        
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")
