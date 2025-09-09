import itchat

from config import conf
from flask import Blueprint, jsonify, request
from common.log import logger
from dto.response import ResultEntity

conf = conf()

blueprint = Blueprint('config', __name__, url_prefix='')


@blueprint.route('/config/getAllChatRoom', methods=['GET'])
def getAllChatRoom():
    list = itchat.get_chatrooms()
    print(list)
    return jsonify(ResultEntity(data=list).to_dict())


@blueprint.route('/config/getAllfriends', methods=['GET'])
def getAllfriends():
    list = itchat.get_friends()
    logger.info("获取所有的getAllfriends")
    print(list)
    # 提取NickName并存储在新列表中
    nicknames = [{"NickName": item["NickName"], 'UserName': item['UserName']} for item in list]
    return jsonify(ResultEntity(data=nicknames).to_dict())


@blueprint.route('/config/sendMessage', methods=['POST'])
def sendMessage():
    data = request.get_json()  # Assumes you're receiving JSON
    logger.info("发送消息:", data)
    message = data['message']
    if data['userName']:
        author = itchat.search_friends(nickName=data['userName'])[0]
        author.send(message)
    if data['userNameId']:
        itchat.send(message, toUserName=data['userNameId'])
    return jsonify(ResultEntity().to_dict())
