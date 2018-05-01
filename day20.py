#!usr/bin/python
错误处理
	Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”

调用栈
	如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：
	# err.py:
	def foo(s):
	    return 10 / int(s)

	def bar(s):
	    return foo(s) * 2

	def main():
	    bar('0')
-.
	main()
	执行，结果如下：

	$ python3 err.py
	Traceback (most recent call last):	#告诉我们这是错误的跟踪信息
	  File "err.py", line 11, in <module>
	    main()	#调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行：
	  File "err.py", line 9, in main
	    bar('0')	#调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
	  File "err.py", line 6, in bar
	    return foo(s) * 2	#调用bar('0')出错了，在代码文件err.py的第9行代码，但原因是第6行：
	  File "err.py", line 3, in foo
	    return 10 / int(s)	#原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了
	ZeroDivisionError: division by zero #原因


	!!!!出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。