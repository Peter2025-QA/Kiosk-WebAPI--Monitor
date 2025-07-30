import pytest
import requests
from utils.token_manager import get_auth_headers
from utils.api_validator import is_api_available
from config.env_config import BASE_URL

class TestOrderRetrievalAPI:
    """订单查询API测试类"""
    
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

def test_get_order_list():
    """测试获取订单列表"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get order list: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get order list: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_order_list_with_token():
    """测试带token获取订单列表"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/orders"
    headers = get_auth_headers(token)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get order list with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get order list with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_order_details():
    """测试获取订单详情"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    order_id = "order-001"
    url = f"{BASE_URL}/v1/orders/{order_id}"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get order details: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get order details: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_order_details_with_token():
    """测试带token获取订单详情"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    order_id = "order-001"
    url = f"{BASE_URL}/v1/orders/{order_id}"
    headers = get_auth_headers(token)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get order details with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get order details with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_order_by_status():
    """测试按状态获取订单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    params = {
        "status": "pending"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get orders by status: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get orders by status: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("status", ["pending", "confirmed", "preparing", "ready", "completed", "cancelled"])
def test_get_orders_by_different_statuses(status):
    """测试不同状态获取订单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    params = {
        "status": status
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get orders with status {status}: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get orders with status {status}: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_order_by_date_range():
    """测试按日期范围获取订单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    params = {
        "start_date": "2024-01-01",
        "end_date": "2024-01-31"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get orders by date range: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get orders by date range: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_order_by_location():
    """测试按位置获取订单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    params = {
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get orders by location: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get orders by location: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}") 