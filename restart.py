import os
from config import conf



port = conf().get("flask_port","8082")

home_dir = os.system(f"./start.sh  {port}")