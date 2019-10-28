'''
Created by auto_sdk on 2019.04.12
'''
from lx_taobaoke.api.base import RestApi
class TbkTpwdCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ext = None
		self.logo = None
		self.text = None
		self.url = None
		self.user_id = None

	def getapiname(self):
		return 'taobao.tbk.tpwd.create'
