from worker.task import Task 
from manager.threadmgr import ThreadManager as Manager

if __name__=="__main__":
	t = Task()
	t.load('task.json')

	m = Manager(3, t.get())
	m.run()
	m.join()
