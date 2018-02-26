from concurrent.futures import ThreadPoolExecutor as Executor, as_completed as AsCompleted
from time import sleep
import random
from spider import spider
from spider import task

def worker(url, actions):
	site = spider.spider(url) 
	site.go(actions)
	sleep(5)

class manager(object):
	def __init__(self, thread_numbers, task):
		self.pool = Executor(thread_numbers)
		self.task = task
		self.futures = {}
	def run(self):
		self.futures = {self.pool.submit(worker, url, actions) : (url, actions) for (url, actions) in self.task}
		for future in AsCompleted(self.futures):
			print(self.futures[future][0])
def main():
	#urls=["www.google.com"]
	#google_actions = [(By.NAME, "q", lambda o: o.send_keys("Faye"), lambda: sleep(1)),
	#		(By.NAME, "btnK", lambda o: o.submit(), lambda: sleep(1) )]
	#actionset =[google_actions]
	#task = zip(urls, actionset)
	b = task.task()
	b.load('task.json')
	print(b.get())
	m = manager(3, b.get())
	m.run()
	#pool = Executor(5)
	#futures = {pool.submit(worker, url, actions): url for url in urls} 
	#for future in AsCompleted(futures):
		#print("now!"+futures[future])

if __name__=="__main__":
	main()
