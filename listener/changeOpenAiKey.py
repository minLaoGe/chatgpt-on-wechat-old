from config import conf
from flask import Blueprint,jsonify

from dto.response import ResultEntity

conf = conf()

blueprint = Blueprint('config', __name__,url_prefix='')



@blueprint.route('/config/changeApiKey/<openKey>', methods=['GET'])
def changeApiKey(openKey):
    conf['open_ai_api_key']=openKey
    print("收到通知更改key",openKey)
    return jsonify(ResultEntity().to_dict())


