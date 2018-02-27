class SimpleManager(object):
	def __init__(self, thread_numbers, worker, task):
		self.worker = worker
		self.task = task
	def run(self):
		for (url, actions, parser_pattern) in self.task:
			self.worker(url, actions, parser_pattern)
	def join(self):
		return
