import os
import sys
import signal
import subprocess

def restart_flask_app():
    flask_process = None
    for line in os.popen("ps ax | grep app_robot.py | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        flask_process = int(pid)

    if flask_process:
        os.kill(flask_process, signal.SIGTERM)
        subprocess.Popen(["python", "app_robot.py"])
    else:
        print("Flask app not found. Starting it...")
        subprocess.Popen(["python", "app_robot.py"])

if __name__ == '__main__':
    restart_flask_app()
