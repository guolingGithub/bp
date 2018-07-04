#coding:utf-8

__author__ = "guoling"

import argparse
import signal
import logging
logger = logging.getLogger('default')

import gevent
from tornado.ioloop import IOLoop
from  gevent.pywsgi import WSGIServer
from gevent.wsgi import WSGIServer

from flask import Flask,jsonify,make_response

misc_service = Flask(__name__)
misc_service.config['JSON_AS_ASCII'] = False
misc_service.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# 导入相应模块并注册蓝图
from Blueprint.Consulting import consulting
misc_service.register_blueprint(consulting, url_prefix='/consulting')

def shutdown():
    logger.stop('stop http server')
    http_server.stop()


def sig_handler(sig,frame):
    logger.warn('Caught signal is %s',sig)
    IOLoop.instance().add_callback(shutdown)


def shutdown():
    logger.debug("Shutting down ...")
    http_server.stop(timeout=5)
    exit(signal.SIGTERM)


@misc_service.route('/healthcheck',methods=['GET'])
def healthcheck():
    return 'MiscServiceBp ok'

@misc_service.route('/',methods=['GET'])
def healthcheck2():
    return 'MiscServiceBp ok'

if __name__ == '__main__':

    # 增加指定端口功能
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--port',type=int, default=6001, help='port providing service')

    args = parser.parse_args()

    #增加信号
    signal.signal(signal.SIGTERM,sig_handler)

    gevent.signal(signal.SIGTERM,shutdown)
    http_server = WSGIServer(('', args.port), misc_service)
    http_server.serve_forever()




