import os
from typing import Dict, Any

class Settings:
    """应用配置类"""
    
    # API配置
    BASE_URL = os.getenv("BASE_URL", "https://staging.orderwithinfi.com/kiosk-shopping-api")
    REALM_ID = os.getenv("REALM_ID", "dev-realm")
    APPZ_ID = os.getenv("APPZ_ID", "kiosk-self-ordering")
    
    # 测试配置
    TEST_TIMEOUT = int(os.getenv("TEST_TIMEOUT", "30"))
    TEST_RETRY_COUNT = int(os.getenv("TEST_RETRY_COUNT", "3"))
    
    # 测试数据配置
    TEST_EMAILS = [
        "test001@infi.us",
        "test002@infi.us", 
        "test003@infi.us"
    ]
    
    TEST_PHONES = [
        "+13124029005",
        "+13124029006",
        "+13124029007"
    ]
    
    TEST_LOCATION_ID = "5382410a-d2d7-4271-a29c-385a38ebbca9"
    
    # 支付配置
    PAYMENT_METHODS = ["card", "cash", "mobile_payment", "gift_card"]
    
    # 订单状态
    ORDER_STATUSES = ["pending", "confirmed", "preparing", "ready", "completed", "cancelled"]
    
    # 通知类型
    NOTIFICATION_TYPES = ["order_update", "payment", "promotion", "system"]
    
    # 积分等级
    REWARD_TIERS = ["bronze", "silver", "gold", "platinum"]
    
    # 菜单分类
    MENU_CATEGORIES = ["main-courses", "appetizers", "desserts", "beverages"]
    
    @classmethod
    def get_test_data(cls) -> Dict[str, Any]:
        """获取测试数据"""
        return {
            "emails": cls.TEST_EMAILS,
            "phones": cls.TEST_PHONES,
            "location_id": cls.TEST_LOCATION_ID,
            "payment_methods": cls.PAYMENT_METHODS,
            "order_statuses": cls.ORDER_STATUSES,
            "notification_types": cls.NOTIFICATION_TYPES,
            "reward_tiers": cls.REWARD_TIERS,
            "menu_categories": cls.MENU_CATEGORIES
        }
    
    @classmethod
    def get_api_config(cls) -> Dict[str, str]:
        """获取API配置"""
        return {
            "base_url": cls.BASE_URL,
            "realm_id": cls.REALM_ID,
            "appz_id": cls.APPZ_ID
        }

# 创建全局配置实例
settings = Settings()
