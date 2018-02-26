import os
import json
from spider import spider

from selenium.webdriver.common.by import By

class task(object):
	def __init__(self):
		self.task = []
	def add(self, url, actions):
		self.task += [(url, actions)] 
	def add_batch(self, urls, actions):
		for url in urls:
			self.add(url, actions)
	def load(self, file):
		sts = json.load(open(file,'r'))
		self.task = []
		for st in sts:
			self.task += [(st[0], spider.unserialize(st[1]))]
	def save(self, file):
		sts = []
		for ts in self.task:
			sts += [(ts[0], spider.serialize(ts[1]))]
		json.dump(sts, open(file,'w')) 
	def get(self):
		return self.task

if __name__ == "__main__":
	url = "http://www.google.com"
	actions = [(By.NAME, "q", lambda o: o.send_keys("Faye"), lambda: sleep(1)),
			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
	a = task()
	a.add(url, actions)
	a.save('task.json')
	b = task()
	b.load('task.json')
	print(b.get())

