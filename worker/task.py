import os
import json
from worker.spider import *
from selenium.webdriver.common.by import By

class Task(object):
	def __init__(self):
		self.task = []
	def add(self, url, actions, parser_pattern):
		self.task += [(url, actions, parser_pattern)] 
	def add_batch(self, urls, actions, parser_pattern):
		for url in urls:
			self.add(url, actions, parser_pattern)
	def load(self, file):
		sts = json.load(open(file,'r'))
		self.task = []
		for st in sts:
			self.task += [(st[0], unserialize(st[1]), st[2])]
	def save(self, file):
		sts = []
		for ts in self.task:
			sts += [(ts[0], serialize(ts[1]), ts[2])]
		json.dump(sts, open(file,'w')) 
	def get(self):
		return self.task

if __name__ == "__main__":
	url = "http://www.google.com"
	actions = [(By.NAME, "q", lambda o: o.send_keys("Faye"), lambda: sleep(1)),
			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
	actions2 = [(By.NAME, "q", lambda o: o.send_keys("Qi"), lambda: sleep(1)),
			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
	
	ancor = {"name" : "div", "class_" : "a-section review"}
	item_patterns = [("star", {"name" : "span", "class_" : "a-coin-alt"}),
			 ("review_title", {"name": "a", "class_" :"a-size-base a-link-normal review-title a-color-base a-text-bold"})
			]
	parser_pattern = { "ancor":ancor, "item_patterns":item_patterns }
	a = Task()
	a.add(url, actions, parser_pattern)
	a.add(url, actions2, parser_pattern)
	a.save('task.json')
	b = Task()
	b.load('task.json')
	print(b.get())

