import threading

balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n


def run_thread(n):
	for i in range(10000):
		# 先要获取锁:
		lock.acquire()
		try:
			# 放心地改吧:
			change_it(n)
		finally:
			# 改完了一定要释放锁:
			lock.release()


if __name__ == '__main__':
	t1 = threading.Thread(target=run_thread, args=(5,))
	t2 = threading.Thread(target=run_thread, args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print('balance: %s' % balance)