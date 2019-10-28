'''
Created on 2012-6-29

@author: lihao
'''
from lx_taobaoke.api.base import sign
from lx_taobaoke.custom_method import LxFunction
from lx_taobaoke.intercept_api import ToaBaoKeApi



class appinfo(object):
    def __init__(self,appkey,secret):
        self.appkey = appkey
        self.secret = secret
        
def getDefaultAppInfo():
    pass

     
def setDefaultAppInfo(appkey,secret):
    default = appinfo(appkey,secret)
    global getDefaultAppInfo 
    getDefaultAppInfo = lambda: default
    




    

