import json

from flask_socketio import emit
from flask import request
import orjson

from utils.gson import to_json

myid = ''
app = ''

def set_app(app_tem):
    global app
    app = app_tem
def setup_events(socketio):

    @socketio.on('connect', namespace='/test')
    def handle_message(data):
        global myid  # 添加这行
        myid = request.sid
        print('received message: ' + str(data))
        emit('test_response', {'data': 'Test response sent'})


    @socketio.on('fuck', namespace='/test')
    def handle_message(data):
        global myid  # 添加这行
        print(myid)
        print('received message: ' + str(data))
        emit('test_response', {'data': 'Test response sent'})



def sendNewMessage(mes,group):
    global myid  # 添加这行
    global app
    if mes.ctype == 'TEXT' or mes.ctype.name == 'TEXT':
        with app.app_context():
            print(f"发送消息:{mes},sid:{myid}")
            if myid:
                json_str = to_json(mes)
                print(json_str)
                emit(f'msg_{group}', json_str, room=myid,namespace='/test')
    elif mes.ctype == 'IMAGE':
        pass

