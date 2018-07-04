#coding:utf-8

__author__ = "guoling"

#返回响应报文 json
def standarlize_response(code,err,biz):
    return {
        'code':code,
        'Description':err,
        'errorDescription':err,
        'dataObject':biz
    }