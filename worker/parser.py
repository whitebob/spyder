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
		entries = self.soup.find_all(**self.ancor)
		aims = []
		for entry in entries:
			data = {}
			for (item, pattern) in self.item_patterns:
				data[item] = entry.find(**pattern)
			aims += data
	def save(self, file):
		json.dump([(self.ancor, self.item_patterns)], open(file,'w'))
	def load(self, file):
		[(self.ancor, self.item_patterns)] = json.load(open(file, 'r'))
	def get(self):
		return self.aims
if __name__ == "__main__":
	ancor = {"name" : "div", "class_" : "a-section review"}
	item_patterns = [("star", {"name" : "span", "class_" : "a-coin-alt"}),
			 ("review_title", {"name": "a", "class_" :"a-size-base a-link-normal review-title a-color-base a-text-bold"})
			]
	a = BS4Parser(ancor, item_patterns)
	a.save('../data/parser.json')
	#b = BS4Parser(None, None)
	#b.load('../data/parser.json')
	#b.save('../data/parser2.json')
