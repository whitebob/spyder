from worker.task import Task
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
	#test case 1
#	url = "https://world.taobao.com"
#	actions = [(By.NAME, "q", lambda o: o.send_keys("wavebetter"), lambda self: sleep(1)),
#			(By.NAME, "q", lambda o: o.submit(), lambda self: (self.switch_status("parse"), sleep(1))),
#			(By.CSS_SELECTOR, "li.item.next > a", lambda o: o.click(), lambda self:(self.switch_redo(True), sleep(1)))
#		]
#	actions2 = [(By.NAME, "q", lambda o: o.send_keys("LG"), lambda self: sleep(1)),
#			(By.NAME, "q", lambda o: o.submit(), lambda self: (self.switch_status("parse"), sleep(1))),
#			(By.CSS_SELECTOR, "li.item.next > a", lambda o: o.click(), lambda self:(self.switch_redo(True), sleep(1)))
#		]
#	ancor = {"name" : "div", "class_" : "item"}
#	item_patterns = [("price", {"name" : "strong"}),
#			 ("count", {"name": "div", "class_" :"deal-cnt"}),
#			 ("shopname", {"name": "a", "class_" :"shopname"})
#			]
#	parser_pattern = {"ancor":ancor, "item_patterns":item_patterns, "output_file":'data/wavebetter.json'}
#	parser_pattern2 = {"ancor":ancor, "item_patterns":item_patterns, "output_file":'data/LG.json'}
#	a = Task()
#	a.add(url, actions, parser_pattern)
#	a.add(url, actions2, parser_pattern2)
#	a.save('data/task.json')
	#test case 2
#	url = "http://www.taobao.com"
#	actions = [(By.NAME, "q", lambda o: o.send_keys("wavebetter"), lambda self: sleep(1), lambda self: () ),
#			(By.NAME, "q", lambda o: o.submit(), lambda self: (self.switch_status("parse"), sleep(1)), lambda self: ()),
#			(By.CSS_SELECTOR, "li.item.next > a", lambda o: o.click(), lambda self:(self.switch_redo(True), sleep(1)), lambda self: () )
#		]
#	ancor = {"name" : "li", "class_": "item next"}
#	item_patterns = [( "next", {"name" : "a"})]
#	parser_pattern = {"ancor":ancor, "item_patterns":item_patterns, "output_file":'data/wavebetter_links.json'}
#	a = Task()
#	a.add(url, actions, parser_pattern)
#	a.save('data/task.json')
	#test case 3
	url = "http://www.taobao.com"
	actions = [(By.NAME, "q", lambda o: o.send_keys("wavebetter"), lambda self: sleep(1), lambda self: () ),
			(By.NAME, "q", lambda o: o.submit(), lambda self: (self.switch_status("parse"), sleep(1)), lambda self: ()),
			(By.CSS_SELECTOR, "li.item.next > a", lambda o: o.click(), lambda self:(self.switch_redo(True), sleep(1)), lambda self: () )
		]
	ancor = {"name" : "div", "class_": "item"}
	item_patterns = [("price", {"name" : "strong"}),
			 ("count", {"name": "div", "class_" :"deal-cnt"}),
			 ("shopname", {"name": "a", "class_" :"shopname"}),
			 ("shoplink", {"name": "a", "class_" :"shopname"}, "href")
			]
	#parser_pattern = {"ancor":ancor, "item_patterns":item_patterns, "output_params":{"output_file":"data/wavebetter_links.json", "output_name":"wavebetter"}}
	parser_pattern = {"ancor":ancor, "item_patterns":item_patterns, "output_params":{"output_db":{"host":"127.0.0.1", "port":27017}, "output_name":"wavebetter"}}
	a = Task()
	a.add(url, actions, parser_pattern)
	a.save('data/task.json')
