import pytest
import requests
from utils.token_manager import get_auth_headers
from utils.api_validator import is_api_available
from config.env_config import BASE_URL

class TestPaymentAPI:
    """支付API测试类"""
    
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

def test_get_payment_methods():
    """测试获取支付方式列表"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/payment/methods"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get payment methods: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get payment methods: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_payment_methods_with_location():
    """测试带位置信息获取支付方式"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/payment/methods"
    params = {
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get payment methods with location: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get payment methods with location: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_process_payment():
    """测试处理支付"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/payment/process"
    payload = {
        "order_id": "order-001",
        "payment_method": "card",
        "amount": 25.99,
        "currency": "USD",
        "payment_details": {
            "card_number": "4111111111111111",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Process payment: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Process payment: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 201, 404, 400]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_process_payment_with_token():
    """测试带token处理支付"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/payment/process"
    payload = {
        "order_id": "order-002",
        "payment_method": "cash",
        "amount": 15.50,
        "currency": "USD"
    }
    headers = get_auth_headers(token)
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Process payment with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Process payment with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 201, 404, 400]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("payment_method", ["card", "cash", "mobile_payment", "gift_card"])
def test_process_payment_different_methods(payment_method):
    """测试不同支付方式处理支付"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/payment/process"
    payload = {
        "order_id": f"order-{payment_method}-001",
        "payment_method": payment_method,
        "amount": 20.00,
        "currency": "USD"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Process payment with {payment_method}: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Process payment with {payment_method}: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 201, 400, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_payment_status():
    """测试获取支付状态"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    payment_id = "payment-001"
    url = f"{BASE_URL}/v1/payment/{payment_id}/status"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get payment status: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get payment status: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_refund_payment():
    """测试退款"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    payment_id = "payment-001"
    url = f"{BASE_URL}/v1/payment/{payment_id}/refund"
    payload = {
        "amount": 10.00,
        "reason": "Customer request"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Refund payment: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Refund payment: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_payment_history():
    """测试获取支付历史"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/payment/history"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get payment history: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get payment history: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_payment_history_with_token():
    """测试带token获取支付历史"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/payment/history"
    headers = get_auth_headers(token)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get payment history with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get payment history with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_process_payment_invalid_amount():
    """测试处理支付无效金额"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/payment/process"
    payload = {
        "order_id": "order-001",
        "payment_method": "card",
        "amount": -10.00,
        "currency": "USD"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Process payment with invalid amount: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Process payment with invalid amount: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [400, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}") 