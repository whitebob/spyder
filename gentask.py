from worker.task import Task
from worker.parser import BS4Parser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
#	url = "http://www.google.com"
#	actions = [(By.NAME, "q", lambda o: o.send_keys("Faye"), lambda: sleep(1)),
#			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
#	actions2 = [(By.NAME, "q", lambda o: o.send_keys("Qi"), lambda: sleep(1)),
#			(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
#	a = Task()
#	a.add(url, actions)
#	a.add(url, actions2)
#	a.save('task.json')
	#b = Task()

	#b.load('task.json')
	#print(b.get())
	#myparser = BS4Parser(None, None)
	#myparser.load('data/parser.json')
	url = "https://world.taobao.com"
	actions = [(By.NAME, "q", lambda o: o.send_keys("Apple"), lambda self: sleep(1)),
			(By.NAME, "q", lambda o: o.submit(), lambda self: (self.switch_status("parse"), sleep(1)))]
	ancor = {"name" : "div", "class_" : "item"}
	item_patterns = [("price", {"name" : "strong"}),
			 ("count", {"name": "div", "class_" :"deal-cnt"}),
			 ("link", {"name": "a", "class_" :"shopname"})
			]
	parser_pattern = {"ancor":ancor, "item_patterns":item_patterns}
	a = Task()
	a.add(url, actions, parser_pattern)
	a.save('data/task.json')
