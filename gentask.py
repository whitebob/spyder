from worker.task import Task
from worker.parser import BS4Parser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":

	#test case 1 
#	url = "https://world.taobao.com"
#	actions = [(By.NAME, "q", lambda o: o.send_keys("LG"), lambda self: sleep(1)),
#			(By.NAME, "q", lambda o: o.submit(), lambda self: (self.switch_status("parse"), sleep(1)))]
#	ancor = {"name" : "div", "class_" : "item"}
#	item_patterns = [("price", {"name" : "strong"}),
#			 ("count", {"name": "div", "class_" :"deal-cnt"}),
#			 ("shopname", {"name": "a", "class_" :"shopname"})
#			]
#	parser_pattern = {"ancor":ancor, "item_patterns":item_patterns}
#	a = Task()
#	a.add(url, actions, parser_pattern)
#	a.save('data/task.json')

	#test case 2
	url = "https://www.taobao.com"
	actions = [(By.NAME, "q", lambda o: o.send_keys("wavebetter"), lambda self: sleep(1)),
			(By.NAME, "q", lambda o: o.submit(), lambda self: (self.switch_status("parse"), sleep(1))),
			(By.CSS_SELECTOR, "li.item.next > a", lambda o: o.click(), lambda self:(self.switch_redo(True), sleep(1)))
		]
	ancor = {"name" : "div", "class_" : "item"}
	item_patterns = [("price", {"name" : "strong"}),
			 ("count", {"name": "div", "class_" :"deal-cnt"}),
			 ("shopname", {"name": "a", "class_" :"shopname"})
			]
	parser_pattern = {"ancor":ancor, "item_patterns":item_patterns}
	a = Task()
	a.add(url, actions, parser_pattern)
	a.save('data/task.json')


