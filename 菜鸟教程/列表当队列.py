from collections import deque

queue=deque(['a','aa','aaa'])
queue.append('aaaa')
queue.append('bbb')
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)