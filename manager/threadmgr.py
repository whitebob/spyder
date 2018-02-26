from concurrent.futures import ThreadPoolExecutor as Executor, as_completed as AsCompleted
from time import sleep
import random
from worker.spider import Spider
from worker.task import Task

def worker(url, actions):
	site = Spider(url) 
	site.go(actions)
	sleep(5)

class ThreadManager(object):
	def __init__(self, thread_numbers, task):
		self.pool = Executor(thread_numbers)
		self.task = task
		self.futures = {}
	def run(self):
		self.futures = {self.pool.submit(worker, url, actions) : (url, actions) for (url, actions) in self.task}
	def join(self):
		for future in AsCompleted(self.futures):
			print(self.futures[future][0])

if __name__=="__main__":
	b = Task()
	b.load('task.json')
	print(b.get())
	m = manager(3, b.get())
	m.run()
	m.join()
