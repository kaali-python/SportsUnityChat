import wand.image 
import base64
import settings
import threading
from common.funcs import S3
import copy
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.py')
class Image(S3):
	def __init__(self, name, content):
		self.name = name
		self.content = content
		self.versions = []

	def version(self):
		self.content = base64.b64decode(self.content)
		image = wand.image.Image(blob = self.content)

		large_version_name = str(self.name) + "/L" + ".jpg"
		image.resize(settings.DP_L_WIDTH, settings.DP_L_HEIGHT)
		self.versions.append({large_version_name: image.make_blob(format='jpg')})

		small_version_name = str(self.name) + "/S" + ".jpg"
		image.resize(settings.DP_S_WIDTH, settings.DP_S_HEIGHT)
		self.versions.append({small_version_name: image.make_blob(format='jpg')})
		
	def handle_upload(self):
		for idx, val in enumerate(self.versions):
			threading.Thread(group = None, target = self.upload_to_s3, name = None, args = (idx, )).start()

	def upload_to_s3(self, index):
		bucket_name = str.strip(config.get('amazon', 'dp_bucket_name'))
		for name, content in self.versions[index].iteritems():
			S3(bucket_name).upload(name, content)
