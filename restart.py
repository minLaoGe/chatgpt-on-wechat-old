import os
import subprocess
from config import conf
import threading
import time
import logging


logger = logging.getLogger('itchat')
def script_to_run():

    location = conf().get("localtion", "")
    # name = conf().get("name", "")
    if not location:
        logger.error(f"路径为空${location}")
        return
    port = conf().get("flask_port", "8082")
    script_name = './startwithPath.sh'
    # 使用 subprocess.Popen 创建一个新的子进程来执行脚本
    subprocess.Popen(['bash', script_name, str(port),location])

def restartcmd():
    logger.error("开始重启脚本.......");
    # 创建一个非守护线程来执行 script_to_run 函数
    non_daemon_thread = threading.Thread(target=script_to_run,daemon=False)
    non_daemon_thread.start()