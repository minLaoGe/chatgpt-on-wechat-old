# 使用官方 Python 运行时作为父镜像
FROM python:3.10.6-slim

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app
COPY ./config-template.json /app/config/config-template.json

RUN pwd
RUN ls -a
# 安装 app.py 所需的任何包
# 如果您有 requirements.txt 文件，请取消注释下一行
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-optional.txt

# 使端口 80 可供此容器外的环境使用
EXPOSE 8080


# 在容器启动时运行 app.py
# 您可以根据需要替换 "app.py" 为您的 Python 文件
CMD ["python", "./app_robot.py"]