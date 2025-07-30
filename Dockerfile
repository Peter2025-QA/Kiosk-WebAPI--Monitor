# API测试框架Docker镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 创建脚本目录
RUN mkdir -p scripts

# 设置执行权限
RUN chmod +x scripts/monitor_api.py

# 暴露端口（如果需要Web界面）
EXPOSE 8080

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from utils.api_validator import is_api_available; exit(0 if is_api_available() else 1)"

# 默认命令
CMD ["python", "scripts/monitor_api.py"] 