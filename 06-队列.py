import queue

# 创建一个队列 括号里面可以传一个数字 表示的是这个队列可以存多少数据
q = queue.Queue(3)

# 存数据
q.put(1)
q.put(2)
q.put(3)
# 当超出队列大小的时候会阻塞
# q.put(4)

data1 = q.get()
print(data1)

data2 = q.get()
print(data2)

data3 = q.get()
print(data3)

q.get(timeout=2)