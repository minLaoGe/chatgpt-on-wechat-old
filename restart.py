import os
import subprocess
from config import conf
import threading
import time
import logging
from lib import itchat

logger = logging.getLogger('itchat')
def script_to_run():
    itchat.logout()  # 登出
    itchat.auto_login(hotReload=True)  # 重新登录

logger.error("开始重启脚本.......");
# 创建一个非守护线程来执行 script_to_run 函数
non_daemon_thread = threading.Thread(target=script_to_run, daemon=False)

non_daemon_thread.start()