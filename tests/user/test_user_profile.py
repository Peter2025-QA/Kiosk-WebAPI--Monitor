import pytest
import requests
from utils.token_manager import get_auth_headers
from utils.api_validator import is_api_available
from config.env_config import BASE_URL

class TestUserProfileAPI:
    """用户资料API测试类"""
    
    def setup_method(self):
        """每个测试方法执行前的设置"""
        if not is_api_available():
            pytest.skip("API不可用")
    
    def make_request(self, method: str, endpoint: str, data: dict = None, 
                    headers: dict = None, params: dict = None, expected_status: list = None):
        """统一的请求处理方法"""
        if not headers:
            headers = get_auth_headers()
        
        url = f"{BASE_URL}{endpoint}"
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, params=params, timeout=10)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data, timeout=10)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=headers, json=data, timeout=10)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=headers, timeout=10)
            else:
                raise ValueError(f"不支持的HTTP方法: {method}")
            
            # 尝试解析JSON响应
            try:
                response_data = response.json()
                print(f"{method} {endpoint}: {response.status_code}, {response_data}")
            except requests.exceptions.JSONDecodeError:
                print(f"{method} {endpoint}: {response.status_code}, 非JSON响应: {response.text}")
                response_data = {"error": "Non-JSON response", "text": response.text}
            
            # 验证状态码
            if expected_status:
                assert response.status_code in expected_status, f"期望状态码 {expected_status}, 实际状态码 {response.status_code}"
            
            return response_data
            
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {e}")

def test_get_user_profile():
    """测试获取用户资料"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/profile"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user profile: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user profile: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_user_profile_with_token():
    """测试带token获取用户资料"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/user/profile"
    headers = get_auth_headers(token)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user profile with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user profile with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_update_user_profile():
    """测试更新用户资料"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/profile"
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone_number": "+13124029005",
        "preferences": {
            "dietary_restrictions": ["vegetarian"],
            "allergies": ["nuts"],
            "favorite_items": ["item-001", "item-002"]
        }
    }
    headers = get_auth_headers()
    
    try:
        response = requests.put(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Update user profile: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Update user profile: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_update_user_profile_with_token():
    """测试带token更新用户资料"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/user/profile"
    payload = {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "phone_number": "+13124029006",
        "preferences": {
            "dietary_restrictions": ["vegan"],
            "allergies": ["dairy"],
            "favorite_items": ["item-003"]
        }
    }
    headers = get_auth_headers(token)
    
    try:
        response = requests.put(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Update user profile with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Update user profile with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_update_user_preferences():
    """测试更新用户偏好设置"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/preferences"
    payload = {
        "dietary_restrictions": ["vegetarian", "gluten_free"],
        "allergies": ["nuts", "shellfish"],
        "favorite_items": ["item-001", "item-002", "item-003"],
        "notification_settings": {
            "email_notifications": True,
            "sms_notifications": False,
            "push_notifications": True
        }
    }
    headers = get_auth_headers()
    
    try:
        response = requests.put(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Update user preferences: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Update user preferences: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_user_preferences():
    """测试获取用户偏好设置"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/preferences"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user preferences: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user preferences: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_user_orders():
    """测试获取用户订单历史"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/orders"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user orders: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user orders: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_user_orders_with_token():
    """测试带token获取用户订单历史"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/user/orders"
    headers = get_auth_headers(token)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user orders with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user orders with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_user_favorites():
    """测试获取用户收藏"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/favorites"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user favorites: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user favorites: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_add_user_favorite():
    """测试添加用户收藏"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/favorites"
    payload = {
        "item_id": "item-001"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Add user favorite: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Add user favorite: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 201, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_remove_user_favorite():
    """测试移除用户收藏"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    item_id = "item-001"
    url = f"{BASE_URL}/v1/user/favorites/{item_id}"
    headers = get_auth_headers()
    
    try:
        response = requests.delete(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Remove user favorite: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Remove user favorite: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_update_user_profile_invalid_email():
    """测试更新用户资料无效邮箱"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/user/profile"
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "invalid-email",
        "phone_number": "+13124029005"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.put(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Update user profile with invalid email: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Update user profile with invalid email: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [400, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}") 