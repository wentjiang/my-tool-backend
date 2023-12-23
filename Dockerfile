# 使用基础镜像
FROM python:3.10.13-slim-bullseye

# 设置工作目录
WORKDIR /app

# 复制应用程序文件到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5001

# 启动应用
CMD ["gunicorn -w 1 -b 0.0.0.0:5001 application:app"]
