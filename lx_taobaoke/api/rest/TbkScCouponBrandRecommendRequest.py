'''
Created by auto_sdk on 2018.11.08
'''
from lx_taobaoke.api.base import RestApi
class TbkScCouponBrandRecommendRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.channel = None
		self.page_no = None
		self.page_size = None
		self.platform = None
		self.site_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.coupon.brand.recommend'
