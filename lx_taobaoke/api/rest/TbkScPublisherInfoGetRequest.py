'''
Created by auto_sdk on 2019.04.19
'''
from lx_taobaoke.api.base import RestApi
class TbkScPublisherInfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.info_type = None
		self.page_no = None
		self.page_size = None
		self.relation_app = None
		self.relation_id = None
		self.special_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.get'
