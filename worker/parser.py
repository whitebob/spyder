from  bs4  import BeautifulSoup
import json
class BS4Parser(object):
	def __init__(self, ancor, item_patterns, output_file):
		self.soup = None
		self.ancor = ancor
		self.item_patterns = item_patterns
		self.aims = []
		self.output_file = output_file
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
			for (item, pattern) in self.item_patterns:
				#print("item:"+item)
				#print(pattern)
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
		print(self.aims)
		json.dump(self.aims, open(self.output_file,'w'))
