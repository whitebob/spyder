from worker.parser import BS4Parser
from worker.spider import Spider 
from worker.task import Task 
from manager.threadmgr import ThreadManager as Manager
#from manager.simplemgr import SimpleManager as Manager
from time import sleep

def myworker(url, actions, parser_pattern):
	myparser = BS4Parser(**parser_pattern)
	site = Spider(url, myparser) 
	site.go(actions)
	myparser.output()
	sleep(3)


if __name__=="__main__":
	t = Task()
	t.load('data/task.json')
	m = Manager(3, myworker, t.get())
	m.run()
	m.join()
