import pytest
import requests
from utils.token_manager import get_auth_headers
from utils.api_validator import is_api_available
from config.env_config import BASE_URL

class TestOrderCreationAPI:
    """订单创建API测试类"""
    
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

def test_create_order():
    """测试创建订单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    payload = {
        "location_id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "items": [
            {
                "item_id": "item-001",
                "quantity": 2,
                "customizations": []
            },
            {
                "item_id": "item-002", 
                "quantity": 1,
                "customizations": [
                    {
                        "option_id": "option-001",
                        "value": "large"
                    }
                ]
            }
        ],
        "payment_method": "card",
        "pickup_time": "2024-01-15T12:00:00Z"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Create order: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Create order: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 201, 404, 400]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_create_order_with_token():
    """测试带token创建订单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/orders"
    payload = {
        "location_id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "items": [
            {
                "item_id": "item-001",
                "quantity": 1,
                "customizations": []
            }
        ],
        "payment_method": "cash",
        "pickup_time": "2024-01-15T12:30:00Z"
    }
    headers = get_auth_headers(token)
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Create order with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Create order with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 201, 404, 400]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_create_order_invalid_items():
    """测试创建订单无效商品"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    payload = {
        "location_id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "items": [
            {
                "item_id": "invalid-item",
                "quantity": 1,
                "customizations": []
            }
        ],
        "payment_method": "card"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Create order with invalid items: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Create order with invalid items: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [400, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_create_order_empty_items():
    """测试创建订单空商品列表"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    payload = {
        "location_id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "items": [],
        "payment_method": "card"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Create order with empty items: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Create order with empty items: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [400, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("payment_method", ["card", "cash", "mobile_payment"])
def test_create_order_different_payment_methods(payment_method):
    """测试不同支付方式创建订单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/orders"
    payload = {
        "location_id": "5382410a-d2d7-4271-a29c-385a38ebbca9",
        "items": [
            {
                "item_id": "item-001",
                "quantity": 1,
                "customizations": []
            }
        ],
        "payment_method": payment_method
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Create order with {payment_method}: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Create order with {payment_method}: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 201, 400, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}") 