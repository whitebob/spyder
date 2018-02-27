Must use python 3.0 for concurent lib, my python is 3.6.4


Use gentask.py to generate the task json. It could be read later on other machines.

```
python3 gentask.py
```

the data structure described  as follows:

url: target_url
actions: = list of  tuple ( find_method, identity, object_action, algo_action )
* here the object_action and algo_action should be in lambda expression to make it easy to serialize

ancor : pattern of each full item in the list. 

item_patterns : define each item and its pattern.

output_file: the final result of each task.




Use test.py to trigger the spider.
```
python3 test.py
```

Added task could be executed concurrently. In the test.py, uncomment the following:

```
from manager.threadmgr import ThreadManager as Manager
```

and comment the following to enable the concurrent feature.

```
from manager.simplemgr import SimpleManager as Manager
```

Use async 
real	3m10.241s
user	0m54.987s
sys	0m7.118sa

Use single thread.
real	3m31.072s
user	0m53.920s
sys	0m7.072s

Because now we only have two tasks and each task is executed in chain. 
If we first get the links and then do the concurrent, it will be much faster.
and we can still have the benefits of "Waiting Random time" for each thread.

