# -*- coding: utf-8 -*-
import lx_taobaoke.api
from lx_taobaoke import LxFunction

class ToaBaoKeApi(object):
    def __init__(self, app_tions, commission_tions):
        self.taobao_api_href = "'http://gw.api.taobao.com'"
        self.app_tions = app_tions
        self.commission_tions = commission_tions

    def get_coupon_api(self, item_id, activity_id):
        '''
        淘宝优惠券接口
        :param item_id: 商品id
        :param activity_id: 优惠券id
        :return:
        '''
        app_tion = LxFunction.get_tion(self.app_tions)
        if not app_tion:
            return {"errer": "app_tions参数错误"}
        req = lx_taobaoke.api.TbkCouponGetRequest()
        req.set_app_info(lx_taobaoke.appinfo(app_tion['appkey'], app_tion['secret']))
        req.item_id = item_id
        req.activity_id = activity_id
        result = req.getResponse()
        url = self.taobao_api_href + result[0]
        text = LxFunction.request_get(url=url, data=result[1], headers=result[2])
        return text

    def get_commission_api(self, item_id):
        '''
        获取佣金接口
        :param item_id: 商品id
        :return:
        '''
        app_tion = LxFunction.get_tion(self.app_tions)
        commission_tion = LxFunction.get_tion(self.commission_tions)
        if not app_tion:
            return {"errer": "app_tions参数错误"}
        if not commission_tion:
            return {"errer": "commission_tions参数错误"}
        req = lx_taobaoke.api.TbkPrivilegeGetRequest()
        req.set_app_info(lx_taobaoke.appinfo(app_tion['appkey'], app_tion['secret']))
        req.item_id = item_id
        req.adzone_id = commission_tion['adzone_id']
        req.site_id = commission_tion['site_id']
        result = req.getResponse(commission_tion['session'])
        url = self.taobao_api_href + result[0]
        text = LxFunction.request_get(url=url, data=result[1], headers=result[2])
        return text

    def get_category_api(self, item_id):
        '''
        获取商品类别
        :param item_id: 商品id
        :return:
        '''
        app_tion = LxFunction.get_tion(self.app_tions)
        if not app_tion:
            return {"errer": "app_tions参数错误"}
        req = lx_taobaoke.api.TbkItemInfoGetRequest()
        req.set_app_info(lx_taobaoke.appinfo(app_tion['appkey'], app_tion['secret']))
        req.num_iids = item_id
        result = req.getResponse()
        url = self.taobao_api_href + result[0]
        text = LxFunction.request_get(url=url, data=result[1], headers=result[2])
        return text