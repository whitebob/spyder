import os
import json
import marshal
import types
import base64

from time import sleep
from selenium import webdriver as  WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class spider(object):
	def __init__(self, url):
		self.driver = WebDriver.Chrome()
		self.url = url
	def go(self, actions):
		self.driver.get(self.url)
		for action in actions:
			action[2](self.driver.find_element(action[0], action[1]))
			action[3]()
	def batch(self, actions):
		self.driver.get(self.url)
		for action in actions:
			for e in self.driver.find_elements(action[0], action[1]):
				action[2](e)
				action[3]()
	def cookies(self):
		for cookie in self.driver.get_cookies():
			print(cookie)
	def quit(self):
		self.driver.quit()

def lambda2str(expr):
	return base64.encodebytes(marshal.dumps(expr.__code__)).decode('ascii')
def str2lambda(strs):
	return types.FunctionType(marshal.loads(base64.decodebytes(strs.encode('ascii'))), globals())

def serialize(actions):
	serialized = []
	for m in actions:
		serialized += [(m[0], m[1], lambda2str(m[2]), lambda2str(m[3]))]
	return serialized

def unserialize(serialized):
	actions = []
	for m in serialized:
		actions += [(m[0], m[1], str2lambda(m[2]), str2lambda(m[3]))]
	return actions

if __name__ == "__main__":
	site = spider("http://www.google.com")
	actions = [(By.NAME, "q", lambda o: o.send_keys("Faye"), lambda: sleep(1)),
			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
	#site.go(actions)
	#site.cookies()
	sa = serialize(actions)
	json.dump(sa, open('a.json','w'))
	sb = json.load(open('a.json','r'))
	deacs = unserialize(sb)
	site.go(deacs)
	sleep(10)
	site.quit()
