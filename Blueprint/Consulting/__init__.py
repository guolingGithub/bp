#coding:utf-8

__author__ = "guoling"

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import config
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
__author__ = 'guoling'
import logging.config
logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger('default')

from flask import Blueprint,jsonify,request
from Common.MessageUtils import standarlize_response

import QueryConsultingCostRules as ConsultingRules

consulting = Blueprint('consult',__name__)


@consulting.route('/bp/consulting/cost/rules',methods=['GET'])
def query_consulting_cost_rules():
    """
    方法用途: 获取副卡-销售品额外信息
    :param: xspid
    :return: json数据
    网页地址测试:
    http://localhost:6001/consulting/bp/consulting/cost/rules?xspid=00000000E0B00375E86F0D16E043AC1410ACB9E7
    """
    logger.debug(u"[查询副卡销售品额外信息接口  start]")
    xspid = request.args.get("xspid", None).strip()   # xspid = request.args.get("xspid").strip()  如果xspid没有 默认的也是None
    if not xspid:
        logger.debug(u"[失败]没有获取到销售品id号")
        return jsonify(standarlize_response(1, u"[失败]没有获取到手机号", None))
    logger.debug(u"[信息]返回结果集")
    result = ConsultingRules.query_consulting_cost_ruless(xspid)
    return result