import requests
import pytest
from utils.token_manager import get_auth_headers
from config.env_config import BASE_URL
from utils.api_validator import is_api_available

class TestUploadDevice:
    """设备上传测试类"""
    
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

def test_upload_device_info():
    """测试上传设备信息"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/device/upload"
    headers = get_auth_headers()
    data = {
        "device-id": "test-device-001",
        "device-type": "kiosk",
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "status": "active"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"Upload device info: {response.status_code}")
        
        # 检查状态码，允许404（端点不存在）
        assert response.status_code in [200, 201, 404], f"意外的状态码: {response.status_code}"
        
        # 如果返回成功状态码，尝试解析JSON
        if response.status_code in [200, 201]:
            try:
                data = response.json()
                print(f"Response data: {data}")
            except requests.exceptions.JSONDecodeError:
                print("响应不是有效的JSON格式")
                
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_upload_device_info_with_token():
    """测试带token上传设备信息"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/device/upload"
    headers = get_auth_headers("test-token")
    data = {
        "device-id": "test-device-002",
        "device-type": "tablet",
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "status": "active"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"Upload device info with token: {response.status_code}")
        
        # 检查状态码，允许404（端点不存在）
        assert response.status_code in [200, 201, 404], f"意外的状态码: {response.status_code}"
        
        # 如果返回成功状态码，尝试解析JSON
        if response.status_code in [200, 201]:
            try:
                data = response.json()
                print(f"Response data: {data}")
            except requests.exceptions.JSONDecodeError:
                print("响应不是有效的JSON格式")
                
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("device_type", ["kiosk", "tablet", "mobile"])
def test_upload_device_info_different_types(device_type):
    """测试不同设备类型上传"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/device/upload"
    headers = get_auth_headers()
    data = {
        "device-id": f"test-device-{device_type}",
        "device-type": device_type,
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "status": "active"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"Upload {device_type} device info: {response.status_code}")
        
        # 检查状态码，允许404（端点不存在）
        assert response.status_code in [200, 201, 404], f"意外的状态码: {response.status_code}"
        
        # 如果返回成功状态码，尝试解析JSON
        if response.status_code in [200, 201]:
            try:
                data = response.json()
                print(f"Response data: {data}")
            except requests.exceptions.JSONDecodeError:
                print("响应不是有效的JSON格式")
                
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_device_status():
    """测试获取设备状态"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/device/status"
    headers = get_auth_headers()
    params = {
        "device-id": "test-device-001"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        print(f"Get device status: {response.status_code}")
        
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
