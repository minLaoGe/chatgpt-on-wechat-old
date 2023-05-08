import os
from config import conf
import signal


signal.signal(signal.SIGPIPE, signal.SIG_DFL)
port = conf().get("flask_port","8082")

home_dir = os.system(f"./start.sh  {port}")