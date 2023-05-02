# encoding:utf-8
from flask import Flask
import threading

import os
from listener import changeOpenAiKey
from config import conf, load_config,load_openai_key
from channel import channel_factory
from common.log import logger
from config import conf, load_config
from plugins import *
import signal
import sys

def sigterm_handler_wrap(_signo):
    old_handler = signal.getsignal(_signo)
    def func(_signo, _stack_frame):
        logger.info("signal {} received, exiting...".format(_signo))
        conf().save_user_datas()
        if callable(old_handler):  #  check old_handler
            return old_handler(_signo, _stack_frame)
        sys.exit(0)

    signal.signal(_signo, func)


def run():
    try:
        # load config
        load_config()


        # ctrl + c
        sigterm_handler_wrap(signal.SIGINT)
        # kill signal
        sigterm_handler_wrap(signal.SIGTERM)

        # create channel
        channel_name = conf().get("channel_type", "wx")

        if "--cmd" in sys.argv:
            channel_name = "terminal"

        if channel_name == "wxy":
            os.environ["WECHATY_LOG"] = "warn"
            # os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = '127.0.0.1:9001'

        channel = channel_factory.create_channel(channel_name)
        if channel_name in ["wx", "wxy", "terminal", "wechatmp", "wechatmp_service"]:
            PluginManager().load_plugins()
        load_openai_key()
        # 创建一个新线程，并指定 worker 函数作为它的目标
        new_thread = threading.Thread(target=start_flask)
        # 启动新线程
        new_thread.start()
        # startup channel
        channel.startup()
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)
def start_flask():
    port = conf().get('flask_port', '8082')
    name = conf().get('flask_name', __name__)
    app = Flask(name)
    app.register_blueprint(changeOpenAiKey.blueprint)

    app.run(host="0.0.0.0", port=port, debug=False)
if __name__ == '__main__':
    run()
