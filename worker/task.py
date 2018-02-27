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

