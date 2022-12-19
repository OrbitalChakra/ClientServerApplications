from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
	def __init__(self, username, password):
		self.client = MongoClient('mongodb://%s:%s@localhost:48399/aac' % (username, password))
		self.database = self.client['aac']
	def create(self, data):
		if data is not None:
			self.database.animals.insert(data)
		else:
			raise Exception("Nothing to save, parameter is empty")
	def read(self, filter):
		curr = self.database.animals.find(filter,{"_id":False})
		if curr:
			return curr
		else:
			raise Exception("Query returned empty result")
	def update(self, filter, data):
		res = self.database.animals.update(filter,data)
		if res:
			return res
		else:
			raise Exception("Query failed")
	def delete(self,filter):
		delete = self.database.animals.delete_one(filter)
		if delete:
			return delete
		else:
			raise Exception("Delete failed")