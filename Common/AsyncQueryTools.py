#coding:utf-8

__author__ = "guoling"
import logging

class AsyncQueryTools:
    def __init__(self):
        self._logger = logging.getLogger('default')

    def async_query(self, sp_name, time_out=15, cache_expires=60, readonly_transaction_required=1,
                    in_param_list=list(), out_param_type_list=list(), db_flag=0):
        '''
        暂时不适合多个存储过程同时调用
        通用查询接口封装
        :param sp_name: 存储过程名称
        :param time_out: 接口超时时间
        :param cache_expires: 缓存失效时间
        :param readonly_transaction_required: 是否支持只读事物
        :param in_param_list: 入参列表（必须按顺序）[['orderid','123456'],['id','123']]
        :param out_param_list: 出参列表
        :param out_param_type_list:出参类型列表
        :return:
        '''
