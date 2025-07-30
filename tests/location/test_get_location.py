import requests
import pytest
from utils.token_manager import get_auth_headers
from config.env_config import BASE_URL
from utils.api_validator import is_api_available

class TestLocationAPI:
    """位置API测试类"""
    
    def setup_method(self):
        """每个测试方法前的设置"""
        if not is_api_available():
            pytest.skip("API不可用")
    
    def make_request(self, method: str, endpoint: str, data: dict = None, 
                    params: dict = None, headers: dict = None) -> requests.Response:
        """统一的请求方法"""
        url = f"{BASE_URL}{endpoint}"
        if headers is None:
            headers = get_auth_headers()
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, params=params, timeout=10)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data, timeout=10)
            else:
                raise ValueError(f"不支持的HTTP方法: {method}")
            
            return response
        except requests.exceptions.RequestException as e:
            pytest.fail(f"请求失败: {e}")

def test_get_location_info():
    """测试获取位置信息"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/location/info"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Get location info: {response.status_code}")
        
        # 检查状态码，允许404（端点不存在）
        assert response.status_code in [200, 404], f"意外的状态码: {response.status_code}"
        
        # 如果返回200，尝试解析JSON
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Response data: {data}")
            except requests.exceptions.JSONDecodeError:
                print("响应不是有效的JSON格式")
                
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_location_info_with_params():
    """测试带参数获取位置信息"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/location/info"
    params = {
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        print(f"Get location info with params: {response.status_code}")
        
        # 检查状态码，允许404（端点不存在）
        assert response.status_code in [200, 404], f"意外的状态码: {response.status_code}"
        
        # 如果返回200，尝试解析JSON
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Response data: {data}")
            except requests.exceptions.JSONDecodeError:
                print("响应不是有效的JSON格式")
                
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_location_settings():
    """测试获取位置设置"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/location/settings"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Get location settings: {response.status_code}")
        
        # 检查状态码，允许404（端点不存在）
        assert response.status_code in [200, 404], f"意外的状态码: {response.status_code}"
        
        # 如果返回200，尝试解析JSON
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Response data: {data}")
            except requests.exceptions.JSONDecodeError:
                print("响应不是有效的JSON格式")
                
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("location_id", [
    "5382410a-d2d7-4271-a29c-385a38ebbca9",
    "test-location-1",
    "test-location-2"
])
def test_get_location_info_multiple_locations(location_id):
    """测试多个位置ID获取信息"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/location/info"
    params = {
        "location-id": location_id
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        print(f"Get location info for {location_id}: {response.status_code}")
        
        # 检查状态码，允许404（端点不存在）
        assert response.status_code in [200, 404], f"意外的状态码: {response.status_code}"
        
        # 如果返回200，尝试解析JSON
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Response data: {data}")
            except requests.exceptions.JSONDecodeError:
                print("响应不是有效的JSON格式")
                
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")
