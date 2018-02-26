import os
import json

from worker.task import Task
from selenium.webdriver.common.by import By

if __name__ == "__main__":
	url = "http://www.google.com"
	actions = [(By.NAME, "q", lambda o: o.send_keys("Faye"), lambda: sleep(1)),
			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
	actions2 = [(By.NAME, "q", lambda o: o.send_keys("Qi"), lambda: sleep(1)),
			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
	a = Task()
	a.add(url, actions)
	a.add(url, actions2)
	a.save('task.json')
	#b = Task()
	#b.load('task.json')
	#print(b.get())

