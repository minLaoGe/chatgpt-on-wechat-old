import json
import os

from config import conf
from flask import Blueprint, jsonify, request
from common.log import logger
from dto.response import ResultEntity
from lib import itchat
import restart
blueprint = Blueprint('config', __name__,url_prefix='')



@blueprint.route('/config/changeApiKey/<openKey>', methods=['GET'])
def changeApiKey(openKey):
    logger.info("收到通知更改key",openKey)
    conf().set('open_ai_api_key',openKey)
    return jsonify(ResultEntity().to_dict())




@blueprint.route('/config/oparate/<oparate>', methods=['GET'])
def oparate(oparate):
    logger.info("收到操作通知key",oparate)
    if oparate not in ['stop', 'restart']:
        return jsonify(ResultEntity().to_dict())
    restart.restartcmd()
    return jsonify(ResultEntity().to_dict())


@blueprint.route('/config/config/modify', methods=['POST'])
def modifyConfig():
    data = request.get_json() # Assumes you're receiving JSON
    logger.info("收到修改参数的通知key={}",data)

    filename= 'config.json'
    config_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir= os.path.dirname(config_dir)
    path = os.path.join(config_dir, filename)
    # 2. 读取配置文件
    try:
        with open(path, 'r',encoding='utf-8') as file:
            config = json.load(file)  # 解析为Python字典
    except Exception as e:
        logger.error(e);

    for key, value in config.items():
        print(f"Key: {key}, Value: {value}")
    # 3. 更新配置项
    if 'mailSender' in data:
        config['mail_sender'] = str(data['mailSender'])
    if 'mailPassword' in data:
        config['mail_password'] = str(data['mailPassword'])
    if 'masterEmails' in data:
        config['master_emails'] = list(data['masterEmails'])
    # 4. 将更新后的配置写回文件
    with open(path, 'w',encoding='utf-8') as file:
        json.dump(config, file, indent=4)

    return jsonify(ResultEntity().to_dict())
