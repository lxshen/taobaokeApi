'''
Created by auto_sdk on 2018.07.25
'''
from lx_taobaoke.api.base import RestApi
class TopAuthTokenCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.code = None
		self.uuid = None

	def getapiname(self):
		return 'taobao.lx_taobaoke.auth.token.create'
