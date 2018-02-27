from concurrent.futures import ThreadPoolExecutor as Executor, as_completed as AsCompleted

class ThreadManager(object):
	def __init__(self, thread_numbers, worker, task):
		self.pool = Executor(thread_numbers)
		self.worker = worker
		self.task = task
		self.futures = {}
	def run(self):
		self.futures = {self.pool.submit(self.worker, url, actions, parser) : (url, actions, parser) for (url, actions, parser) in self.task}
	def join(self):
		for future in AsCompleted(self.futures):
			print(self.futures[future][0])

