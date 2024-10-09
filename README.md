创建虚拟环境 python -m venv venv

激活虚拟环境 venv\Scripts\activate

虚拟环境中安装ASGI服务器 pip install fastapi uvicorn

新建 main.py文件

终端启动服务 uvicorn main:app --reload
