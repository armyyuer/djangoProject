'''
Created by auto_sdk on 2021.06.24
'''
from dingtalk.api.base import RestApi
class OapiRhinoMosExecClothesGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.entity_ids = None
		self.order_id = None
		self.tenant_id = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.mos.exec.clothes.get'
