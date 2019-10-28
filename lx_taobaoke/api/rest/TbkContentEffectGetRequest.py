'''
Created by auto_sdk on 2018.07.25
'''
from lx_taobaoke.api.base import RestApi
class TbkContentEffectGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.option = None

	def getapiname(self):
		return 'taobao.tbk.content.effect.get'
