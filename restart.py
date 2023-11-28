import os
import subprocess
from config import conf
import threading
import time
import logging
from lib import itchat
from utils.EmailUtils import send_email
import io

logger = logging.getLogger('itchat')


def qrCallback(uuid, status, qrcode):
    # logger.debug("qrCallback: {} {}".format(uuid,status))
    if status == "0":
        try:
            from PIL import Image

            img = Image.open(io.BytesIO(qrcode))
            _thread = threading.Thread(target=img.show, args=("QRCode",))
            _thread.setDaemon(True)
            _thread.start()
        except Exception as e:
            pass

        import qrcode

        url = f"https://login.weixin.qq.com/l/{uuid}"

        qr_api1 = "https://api.isoyu.com/qr/?m=1&e=L&p=20&url={}".format(url)
        qr_api2 = (
            "https://api.qrserver.com/v1/create-qr-code/?size=400×400&data={}".format(
                url
            )
        )
        qr_api3 = "https://api.pwmqr.com/qrcode/create/?url={}".format(url)
        qr_api4 = "https://my.tv.sohu.com/user/a/wvideo/getQRCode.do?text={}".format(
            url
        )
        print("You can also scan QRCode in any website below:")
        print(qr_api3)
        send_email(url,qr_api3)
        print(qr_api4)
        print(qr_api2)
        print(qr_api1)

        qr = qrcode.QRCode(border=1)
        qr.add_data(url)
        qr.make(fit=True)
        qr.print_ascii(invert=True)


def script_to_run():
    itchat.logout()  # 登出
    itchat.auto_login(enableCmdQR=2,qrCallsback=qrCallback)  # 重新登录

logger.error("开始重启脚本.......");
# 创建一个非守护线程来执行 script_to_run 函数
non_daemon_thread = threading.Thread(target=script_to_run, daemon=False)

non_daemon_thread.start()