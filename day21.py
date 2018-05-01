#!/usr/bin/python
调试
	函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。
		>>> def foo():
		r = some_function()
		if r==(-1):
			return (-1)
		#do something
		return r

		>>> def bar():
			r = foo()
			if r==(-1):
				print('Error')
			else:
				
	try:
		pass
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass

	>>> try:
		print('try..')
		r = 10 / 0	#有错误, 跳转至E
		print('result:', r)#被跳过
	except ZeroDivisionError as e:
		print('except:', e)
	finally:
		print('finally..')
		print('END')

		
	try..
	except: division by zero
	finally..
	END

	>>> try:	#无错误
		print('try..')
		r = 10 / 2
		print('result:', r)
	except ZeroDivisionError as e:#被跳过
		print('except:', e)
	finally:
		print('finally..')
		print('END')

		
	try..
	result: 5.0
	finall

	# 也可以增加多条except
	try:
	    print('try...')
	    r = 10 / int('a')
	    print('result:', r)
	except ValueError as e:
	    print('ValueError:', e)
	except ZeroDivisionError as e:
	    print('ZeroDivisionError:', e)
	#else:	#else用法
		#print('no error!')
	finally:
	    print('finally...')
	print('END')


	try...
	ValueError: invalid literal for int() with base 10: 'a'
	#no error! 
	finally...
	END

	# 可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句

	使用try...except 捕获错误还有一个巨大的好处，就是可以跨越多层调用，
	即函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
	>>> def foo(s):
	    return 10 / int(s)

	>>> def bar(s):
	    return foo(s) * 2

	>>> def main():
	    try:
	        bar('0')
	    except Exception as e:
	        print('Error:', e)
	    finally:
	        print('finally...')

	>>> foo(6)
	1.6666666666666667
	>>> foo(5)
	2.0
	>>> bar(5)
	4.0
	>>> bar(10)
	2.0
	>>> main(5)
	Traceback (most recent call last):
	  File "<pyshell#56>", line 1, in <module>
	    main(5)
	TypeError: main() takes 0 positional arguments but 1 was given
	#不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以
	#以上

调用栈
	# 分析错误
	出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置
记录错误
	Python内置的logging模块可以非常容易地记录错误信息：
	# err_logging.py

	import logging

	def foo(s):
	    return 10 / int(s)

	def bar(s):
	    return foo(s) * 2

	def main():
	    try:
	        bar('0')
	    except Exception as e:
	        logging.exception(e)

	main()
	print('END')
	同样是出错，但程序打印完错误信息后会继续执行，并正常退出：

	$ python3 err_logging.py#day
	ERROR:root:division by zero

抛出错误
	

