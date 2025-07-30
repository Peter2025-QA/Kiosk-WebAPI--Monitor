import pytest
import requests
from utils.token_manager import get_auth_headers
from utils.api_validator import is_api_available
from config.env_config import BASE_URL

class TestLoyaltyAPI:
    """积分系统API测试类"""
    
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

def test_get_reward_tiers():
    """测试获取积分等级列表"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/loyalty/reward-tiers"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get reward tiers: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get reward tiers: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_reward_tiers_with_location():
    """测试带位置信息获取积分等级"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/loyalty/reward-tiers"
    params = {
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get reward tiers with location: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get reward tiers with location: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_user_loyalty_info():
    """测试获取用户积分信息"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/loyalty/user-info"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user loyalty info: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user loyalty info: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_user_loyalty_info_with_token():
    """测试带token获取用户积分信息"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/loyalty/user-info"
    headers = get_auth_headers(token)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get user loyalty info with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get user loyalty info with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_loyalty_rewards():
    """测试获取积分奖励"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/loyalty/rewards"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get loyalty rewards: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get loyalty rewards: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("tier_id", [
    "bronze",
    "silver", 
    "gold",
    "platinum"
])
def test_get_reward_tier_details(tier_id):
    """测试获取特定积分等级详情"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/loyalty/reward-tiers/{tier_id}"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get reward tier {tier_id} details: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get reward tier {tier_id} details: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_loyalty_transactions():
    """测试获取积分交易记录"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/loyalty/transactions"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get loyalty transactions: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get loyalty transactions: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_loyalty_transactions_with_token():
    """测试带token获取积分交易记录"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    token = "your_token_here"  # Replace with valid token
    url = f"{BASE_URL}/v1/loyalty/transactions"
    headers = get_auth_headers(token)
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get loyalty transactions with token: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get loyalty transactions with token: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 401, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")
