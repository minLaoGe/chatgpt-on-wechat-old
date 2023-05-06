from config import conf
from flask import Blueprint,jsonify
from common.log import logger
from dto.response import ResultEntity




blueprint = Blueprint('config', __name__,url_prefix='')



@blueprint.route('/config/changeApiKey/<openKey>', methods=['GET'])
def changeApiKey(openKey):
    logger.info("收到通知更改key",openKey)
    conf().set('open_ai_api_key',openKey)
    return jsonify(ResultEntity().to_dict())


