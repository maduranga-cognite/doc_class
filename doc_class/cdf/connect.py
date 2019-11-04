class Con:

	def getaccess(self):
		from cognite.client import CogniteClient
		import os

		c = CogniteClient(api_key=os.environ['PUBLICDATA_API_KEY'], client_name=os.environ['PUBLICDATA_API_KEY'])
		c.login.status()







	