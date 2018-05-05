#!usr/bin/python
进程和线程
	对于操作系统来说，一个任务就是一个进程（Process）
	把进程内的子任务称为线程（Thread）

	执行多任务方案
		多进程模式；
		多线程模式；
		多进程+多线程模式。
	
	线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
	多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂

多进程（multiprocessing）
		Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
	因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
	子进程永远返回0，而父进程返回子进程的ID。
	一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

	getppid()	#就可以拿到父进程的ID
	
	在os模块就封装了常见的系统调用包括fork
	import os

	print('Process (%s) start...' % os.getpid())
	# Only works on Unix/Linux/Mac:
	pid = os.fork()
	if pid == 0:
	    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
	else:
	    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

	Process (876) start...
	I (876) just created a child process (877).
	I am child process (877) and my parent is 876.

	很遗憾我是windows
	# >>> import os
	# >>> print('Process (%s) start...' % os.getpid())
	# Process (11576) start...
	# >>> pid = os.fork()	#Windows没有fork调用
	# Traceback (most recent call last):
	#   File "<pyshell#2>", line 1, in <module>
	#     pid = os.fork()
	# AttributeError: module 'os' has no attribute 'fork'
	mac没有问题

multiprocessing
	multiprocessing模块提供了一个Process类来代表一个进程对象, 
	# 下面的例子演示了启动一个子进程并等待其结束
	#day26try.py
	from multiprocessing import Process
	import os

	# 子进程要执行的代码
	def run_proc(name):
	    print('Run child process %s (%s)...' % (name, os.getpid()))

	if __name__=='__main__':
	    print('Parent process %s.' % os.getpid())
	    p = Process(target=run_proc, args=('test',))
	    print('Child process will start.')
	    p.start()	#start()方法启动
	    p.join()	#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	    print('Child process end.')

	#py day26try.py	
	Parent process 13296.
	Process will start.
	Run child process test (11464)...
	Process end.

Pool
	如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
	#pool.py
	from multiprocessing import Pool
	import os, time, random

	def long_time_task(name):
	    print('Run task %s (%s)...' % (name, os.getpid()))
	    start = time.time()
	    time.sleep(random.random() * 3)
	    end = time.time()
	    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

	if __name__=='__main__':
	    print('Parent process %s.' % os.getpid())
	    p = Pool(4)
	    for i in range(5):
	        p.apply_async(long_time_task, args=(i,))
	    print('Waiting for all subprocesses done...')
	    p.close()	#调用close()之后就不能继续添加新的Process了
	    p.join()	#对Pool对象调用join()方法会等待所有子进程执行完毕, 必须先调用close()
    print('All subprocesses done.')

    #py pool.py
    Parent process 669.
	Waiting for all subprocesses done...
	Run task 0 (671)...
	Run task 1 (672)...
	Run task 2 (673)...
	Run task 3 (674)...
	Task 2 runs 0.14 seconds.
	Run task 4 (673)...
	Task 1 runs 0.27 seconds.
	Task 3 runs 0.86 seconds.
	Task 0 runs 1.41 seconds.
	Task 4 runs 1.91 seconds.
	All subprocesses done.
	# task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
	# Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程

	p = Pool(5)	#可以同时跑5个进程。
	# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
	so, 我是四核?

子进程
	很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
	subprocess模块可以启动一个子进程, 控制其输入或输出
	# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
	#day26try2.py
	import subprocess

	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('Exit code:', r)

	#py day26try2.py #以下是例子  cmd复制不了
	$ nslookup www.python.org
	Server:        192.168.19.4
	Address:    192.168.19.4#53

	Non-authoritative answer:
	www.python.org    canonical name = python.map.fastly.net.
	Name:    python.map.fastly.net
	Address: 199.27.79.223

	Exit code: 0

	#pycharm
	$ nslookup www.python.org
	��Ȩ��Ӧ��:
	������#服务器:  UnKnown
	Address:  192.168.43.1

	����#名称:    dualstack.python.map.fastly.net
	Addresses:  2a04:4e42:11::223
		  151.101.228.223
	Aliases:  www.python.org

	Exit code: 0

	# 如果子进程还需要输入，则可以通过communicate()方法输入：
	import subprocess

	print('$ nslookup')
	p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
	print(output.decode('utf-8'))
	print('Exit code:', p.returncode)
	# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：

	set q=mx
	python.org
	exit

	# 运行结果
	$ nslookup
	Server:        192.168.19.4
	Address:    192.168.19.4#53

	Non-authoritative answer:
	python.org    mail exchanger = 50 mail.python.org.

	Authoritative answers can be found from:
	mail.python.org    internet address = 82.94.164.166
	mail.python.org    has AAAA address 2001:888:2000:d::a6


	Exit code: 0

	#我的失败了, 不知道是什么原因

进程间通信
	multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

	#以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
	#day26try3.py
	from multiprocessing import Process, Queue
	import os, time, random

	# 写数据进程执行的代码:
	def write(q):
	    print('Process to write: %s' % os.getpid())
	    for value in ['A', 'B', 'C']:
	        print('Put %s to queue...' % value)
	        q.put(value)
	        time.sleep(random.random())

	# 读数据进程执行的代码:
	def read(q):
	    print('Process to read: %s' % os.getpid())
	    while True:
	        value = q.get(True)
	        print('Get %s from queue.' % value)

	if __name__=='__main__':
	    # 父进程创建Queue，并传给各个子进程：
	    q = Queue()
	    pw = Process(target=write, args=(q,))
	    pr = Process(target=read, args=(q,))
	    # 启动子进程pw，写入:
	    pw.start()
	    # 启动子进程pr，读取:
	    pr.start()
	    # 等待pw结束:
	    pw.join()
	    # pr进程里是死循环，无法等待其结束，只能强行终止:
	    pr.terminate()

	#运行
	Process to write: 15692
	Put A to queue...
	Process to read: 15700
	Get A from queue.
	Put B to queue...
	Get B from queue.
	Put C to queue...
	Get C from queue.

		在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
	由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

	在Unix/Linux下，可以使用fork()调用实现多进程。

	要实现跨平台的多进程，可以使用multiprocessing模块。

	进程间通信是通过Queue、Pipes等实现的。