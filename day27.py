#!/usr/bin/python
多线程
	# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
	由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
	
	_thread和threading，_thread是低级模块，threading是高级模块，
	# 对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
	启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
	#day27thread.py

	# 运行
	C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day27thread.py
	thread MainThread is running...
	thread LoopThread is running...
	thread LoopThread >>> 1
	thread LoopThread >>> 2
	thread LoopThread >>> 3
	thread LoopThread >>> 4
	thread LoopThread >>> 5
	thread LoopThread ended.
	thread MainThread ended.

	current_thread() #函数永远返回当前线程的实例
	#t = threading.Thread(target=loop, name='LoopThread')


Lock
	多线程和多进程最大的不同在于同一个变量, 前者共享一个, 后者在每个进程都有拷贝互不影响

	# day27try.py #多个线程同时操作一个变量
	import time, threading

	# 假定这是你的银行存款:
	balance = 0

	def change_it(n):
	    # 先存后取，结果应该为0:
	    global balance
	    balance = balance + n
	    balance = balance - n

	def run_thread(n):
	    for i in range(100000):
	        change_it(n)

	t1 = threading.Thread(target=run_thread, args=(5,))
	t2 = threading.Thread(target=run_thread, args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)

	# 运行结果为0, 但是多运行几次会变
	
	定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
	原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
	balance = balance + n
	分两步
		1.x = balance + n	#计算balance + n，存入临时变量中；
		2.balance = x 	#将临时变量的值赋给balance。

	原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
	要确保balance计算正确，就要给change_it()上一把锁该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突

	threading.Lock() #创建一个锁
	#day27try2.py #加了锁的版本-多进程

		当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
	获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。

	优缺点
		锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

	多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
	Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。	

ThreadLocal
	在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
	局部变量也有问题，就是在函数调用的时候，传递起来很麻烦

	#day27try3.py #	ThreadLocal

	运行结果
	Hello, Alice (in Thread-A)
	Hello, Bob (in Thread-B)

	全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

	可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。

	//ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

小结
	一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题