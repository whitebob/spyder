
Use gentask.py to generate the task.

Use test.py to trigger the spider.


Use async 
real	3m10.241s
user	0m54.987s
sys	0m7.118sa

Use single thread.
real	3m31.072s
user	0m53.920s
sys	0m7.072s

Because now we only have two task and each task is executed in chain. 
If we first get the links and then do the concurrent, it will be much faster.
and we can still have the benifets of "Waiting Random time" for each thread.

