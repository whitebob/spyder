from  bs4  import BeautifulSoup
import json
from pymongo import MongoClient as Client

class BS4Parser(object):
	def __init__(self, ancor, item_patterns, output_params):
		self.soup = None
		self.ancor = ancor
		self.item_patterns = item_patterns
		self.aims = []
		self.output_params = output_params
	def parse(self, page):
		self.soup = BeautifulSoup(page,"lxml")
		try:
			entries = self.soup.find_all(**self.ancor)
		except:
			print("ancor not found!")
			return
		#self.aims = []
		print("Found "+str(len(entries))+" entries!")
		for entry in entries:
			data = {}
			for (item, pattern, *method) in self.item_patterns:
				print("item:"+item)
				print(pattern)
				if method :
					print(method)
					try:
						m = method[0]
						if   m == "href": 
							data[item] = entry.find(**pattern)['href']
						elif m == "text":
							data[item] = entry.find(**pattern).text
						elif m == "attribute":
							data[item] = entry.find(**pattern)[method[1]]
						elif m == "pretty":
							data[item] = entry.find(**pattern).prettify()
						#need serializatoin for lambda expression
						#elif m == "custom":
						#	data[item] = method[1](entry.find(**pattern).string)
						else:
							data[item] = entry.find(**pattern).text
					except:
						print("No pattern in current entry")
						continue
				else:
					try:
						data[item] = entry.find(**pattern).text
					except:
						print("No pattern in current entry")
						continue
			self.aims.append(data)
			print(data)
		#print(self.aims)
	def get(self):
		return self.aims
	def output(self):
		if not self.output_params:
			print(self.aims)
		elif self.output_params.get('output_file'):
			try:	
				print("Output to file"+self.output_params['output_file'])
				result = {}
				result[self.output_params['output_name']] = self.aims
				json.dump(result, open(self.output_params['output_file'],'w'))
			except:
				print("Error on json dump")
		elif self.output_params.get('output_db'):
			try:	
				db = Client(**self.output_params['output_db']).spyder
				collection = db[self.output_params['output_name']]
				collection.insert_many(self.aims)
			except:
				print("Error on db output")
		else:
			print("No valid output parameters found!")

