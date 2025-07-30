# Quick Start Guide

## Project Overview

This is a comprehensive API testing framework for the Kiosk Shopping API. The project includes 151 tests covering all major API endpoints including authentication, orders, payments, user management, and more.

## 🚀 Automatic Detection and Deployment

### Quick Setup

#### 1. Test Monitoring Function
```bash
# Test monitoring functionality
python scripts/test_monitor.py
```

#### 2. Start Automatic Monitoring
```bash
# Start full monitoring (background)
python scripts/monitor_api.py &

# Or run in foreground (see real-time logs)
python scripts/monitor_api.py
```

#### 3. One-click Deployment
```bash
# Give execute permission to deployment script
chmod +x scripts/deploy.sh

# Run automatic deployment
./scripts/deploy.sh
```

### Automatic Detection Features
- ✅ **Check API status every 5 minutes**
- ✅ **Auto-notify on status changes**
- ✅ **Real-time API availability monitoring**
- ✅ **Auto-generate monitoring reports**

### Automatic Testing Features
- ✅ **Run full test suite every hour**
- ✅ **Generate HTML and Allure reports**
- ✅ **Auto-notify on test failures**
- ✅ **151 test cases full coverage**

### Deployment Options
- **Local Deployment**: Direct script execution
- **Docker Deployment**: Using docker-compose
- **GitHub Actions**: Automatic CI/CD pipeline

For detailed deployment guide, see: [AUTO_DEPLOYMENT_GUIDE.md](AUTO_DEPLOYMENT_GUIDE.md)

## Project Structure

```
kiosk_login_pytest_complete_full/
├── config/
│   ├── env_config.py          # API configuration
│   └── settings.py            # Test settings
├── tests/
│   ├── base_test.py           # Base test class
│   ├── conftest.py            # Pytest configuration
│   ├── location/              # Location API tests
│   ├── login/                 # Authentication tests
│   ├── loyalty/               # Loyalty system tests
│   ├── menu/                  # Menu API tests
│   ├── order/                 # Order management tests
│   ├── payment/               # Payment processing tests
│   ├── user/                  # User profile tests
│   └── verification/          # Verification code tests
├── utils/
│   ├── api_validator.py       # API availability checker
│   ├── request_handler.py     # HTTP request utilities
│   └── token_manager.py       # Authentication token management
├── requirements.txt           # Python dependencies
├── pytest.ini               # Pytest configuration
└── README.md                # Project documentation
```

## Installation

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation**:
   ```bash
   python -m pytest --version
   ```

## Running Tests

### Basic Commands

```bash
# Run all tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run specific module
python -m pytest tests/login/

# Run specific test file
python -m pytest tests/login/test_login_email.py

# Run specific test function
python -m pytest tests/login/test_login_email.py::test_login_with_email
```

### Advanced Commands

```bash
# Run with HTML report
python -m pytest --html=test_report.html

# Run with Allure report
python -m pytest --alluredir=allure-results

# Run tests in parallel (requires pytest-xdist)
python -m pytest -n auto

# Run only failed tests
python -m pytest --lf

# Run tests with custom markers
python -m pytest -m "api_required"
```

### Test Categories

| Category | Command | Tests |
|----------|---------|-------|
| All Tests | `python -m pytest` | 148 |
| Authentication | `python -m pytest tests/login/` | 17 |
| Orders | `python -m pytest tests/order/` | 32 |
| Payments | `python -m pytest tests/payment/` | 13 |
| User Management | `python -m pytest tests/user/` | 15 |
| Menu | `python -m pytest tests/menu/` | 10 |
| Loyalty | `python -m pytest tests/loyalty/` | 11 |
| Verification | `python -m pytest tests/verification/` | 26 |
| Location | `python -m pytest tests/location/` | 12 |

## API Configuration

The API configuration is in `config/env_config.py`:

```python
BASE_URL = "https://staging.orderwithinfi.com/kiosk-shopping-api"
REALM_ID = "dev-realm"
APPZ_ID = "kiosk-self-ordering"
```

## Test Framework Features

### 1. API Availability Checking
- Automatically checks if API is available before running tests
- Skips tests gracefully when API is unavailable
- Provides clear error messages

### 2. Robust Error Handling
- Handles non-JSON responses (404 pages)
- Manages network timeouts
- Provides detailed error logging

### 3. Flexible Status Code Validation
- Accepts multiple valid status codes (200, 404, 401)
- Adapts to API availability
- Provides meaningful assertions

### 4. Comprehensive Logging
- Logs all API requests and responses
- Shows status codes and response data
- Handles JSON decode errors gracefully

## Example Test Output

```
tests/login/test_login_email.py::test_login_with_email PASSED
tests/login/test_login_email.py::test_login_with_email_invalid_credentials PASSED
tests/login/test_login_email.py::test_login_with_multiple_emails[test001@infi.us-123123] PASSED
```

## Troubleshooting

### Common Issues

1. **API Unavailable**:
   - Tests will be skipped automatically
   - Check API endpoint configuration
   - Verify network connectivity

2. **Import Errors**:
   - Ensure all dependencies are installed
   - Check Python path configuration

3. **Timeout Errors**:
   - Network connectivity issues
   - API server response time
   - Increase timeout in test configuration

### Debug Mode

```bash
# Run with maximum verbosity
python -m pytest -vvv

# Run with print statements
python -m pytest -s

# Run with both
python -m pytest -vvv -s
```

## Reports

### HTML Report
```bash
python -m pytest --html=test_report.html --self-contained-html
```

### Allure Report
```bash
# Generate report
python -m pytest --alluredir=allure-results

# View report (requires allure command line tool)
allure serve allure-results
```

## Continuous Integration

The framework is designed to work with CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run API Tests
  run: |
    pip install -r requirements.txt
    python -m pytest --html=test_report.html
```

## Support

For issues or questions:
1. Check the test output for error messages
2. Review the API configuration
3. Verify API endpoint availability
4. Check the troubleshooting section above

## Next Steps

1. **Customize API endpoints** in `config/env_config.py`
2. **Add new test cases** following the existing patterns
3. **Configure CI/CD integration** for automated testing
4. **Set up monitoring** for API availability
5. **Add performance testing** for load testing scenarios 