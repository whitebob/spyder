from  bs4  import BeautifulSoup
import json
class BS4Parser(object):
	def __init__(self, ancor, item_patterns):
		self.soup = None
		self.ancor = ancor
		self.item_patterns = item_patterns
		self.aims = []
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
	def output(self, file):
		print(self.aims)
		json.dump(self.aims, open(file,'w'))
if __name__ == "__main__":
	ancor = {"name" : "div", "class_" : "a-section review"}
	item_patterns = [("star", {"name" : "span", "class_" : "a-coin-alt"}),
			 ("review_title", {"name": "a", "class_" :"a-size-base a-link-normal review-title a-color-base a-text-bold"})
			]
	a = BS4Parser(ancor, item_patterns)
	#b = BS4Parser(None, None)
	#b.load('../data/parser.json')
	#b.save('../data/parser2.json')
