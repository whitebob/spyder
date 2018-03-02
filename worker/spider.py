import os
import json
import marshal
import types
import base64

from time import sleep
from selenium import webdriver as  WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class Spider(object):
	def __init__(self, url, parser):
		self.status = "ready"
		#options = WebDriver.ChromeOptions()
		#options.add_argument('headless')
		#self.driver = WebDriver.Chrome(chrome_options=options)
		self.driver = WebDriver.Chrome()
		self.url = url
		self.parser = parser
		self.redo = False
	def go(self, actions):
		self.driver.get(self.url)
		self.status ="go"
		for action in actions:
			if self.status == "stop" :
				#self.quit()
				break
			while True:
				try:
					action[2](self.driver.find_element(action[0], action[1]))
					action[3](self)
					print("Found "+action[0]+":"+action[1]+"! and success command executed.")
				except:
					self.status = "stop"
					action[4](self)
					print(action[0]+":"+action[1]+" not found! and failure command executed.")
				print("Status: " + self.status)
				print("Redo: " + str(self.redo))
				if self.status == "parse":
					self.parser.parse(self.get_page_s())
				if self.status == "stop":
					self.redo = False
				if not self.redo:
					break
	def switch_status(self, status):
		self.status = status
	def switch_redo(self, redo):
		self.redo = redo
	def cookies(self):
		for cookie in self.driver.get_cookies():
			print(cookie)
	def get_page_s(self):
		return self.driver.execute_script('return document.documentElement.outerHTML;')
	def get_page(self):
		return self.driver.page_source
	def quit(self):
		self.driver.quit()
	def scroll_down(self):
		self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
	def switch_tab(self):
		self.driver.switch_to.window(self.driver.window_handles[1])
def lambda2str(expr):
	return base64.encodebytes(marshal.dumps(expr.__code__)).decode('ascii')
def str2lambda(strs):
	return types.FunctionType(marshal.loads(base64.decodebytes(strs.encode('ascii'))), globals())

def serialize(actions):
	serialized = []
	for m in actions:
		serialized += [(m[0], m[1], lambda2str(m[2]), lambda2str(m[3]), lambda2str(m[4]))]
	return serialized

def unserialize(serialized):
	actions = []
	for m in serialized:
		actions += [(m[0], m[1], str2lambda(m[2]), str2lambda(m[3]), str2lambda(m[4]))]
	return actions

