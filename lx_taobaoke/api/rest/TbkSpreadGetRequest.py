'''
Created by auto_sdk on 2018.11.16
'''
from lx_taobaoke.api.base import RestApi
class TbkSpreadGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.requests = None

	def getapiname(self):
		return 'taobao.tbk.spread.get'
