import pytest
import requests
from utils.token_manager import get_auth_headers
from utils.api_validator import is_api_available
from config.env_config import BASE_URL

class TestMenuAPI:
    """菜单API测试类"""
    
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

def test_get_menu_categories():
    """测试获取菜单分类"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/menu/categories"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get menu categories: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get menu categories: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_menu_items():
    """测试获取菜单项目"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/menu/items"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get menu items: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get menu items: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_menu_items_by_category():
    """测试按分类获取菜单项目"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/menu/items"
    params = {
        "category_id": "main-courses"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get menu items by category: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get menu items by category: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_menu_item_details():
    """测试获取菜单项目详情"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    item_id = "item-001"
    url = f"{BASE_URL}/v1/menu/items/{item_id}"
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        try:
            response_data = response.json()
            print(f"Get menu item details: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get menu item details: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

@pytest.mark.parametrize("category_id", [
    "main-courses",
    "appetizers", 
    "desserts",
    "beverages"
])
def test_get_menu_items_multiple_categories(category_id):
    """测试多个分类获取菜单项目"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/menu/items"
    params = {
        "category_id": category_id
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get menu items for category {category_id}: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get menu items for category {category_id}: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_get_menu_with_location():
    """测试带位置信息获取菜单"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/menu/items"
    params = {
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Get menu with location: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Get menu with location: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")

def test_search_menu_items():
    """测试搜索菜单项目"""
    if not is_api_available():
        pytest.skip("API不可用")
    
    url = f"{BASE_URL}/v1/menu/search"
    params = {
        "query": "burger",
        "location-id": "5382410a-d2d7-4271-a29c-385a38ebbca9"
    }
    headers = get_auth_headers()
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        try:
            response_data = response.json()
            print(f"Search menu items: {response.status_code}, {response_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"Search menu items: {response.status_code}, 非JSON响应: {response.text}")
        assert response.status_code in [200, 404, 401]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"请求失败: {e}")
