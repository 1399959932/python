#!usr/bin/python
# print('今天面试了商家3.13')

生成器, generator
	一边循环一边计算的机制，称为生成器：generator
	生成一个generator:
		# page1
		只要把一个列表生成式的[]改成()，就创建了一个generator：
	>>> L = [x * x for x in range(10)] #列表生成式生成list, L
	>>> L #list
	[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
	>>> G = (x * x for x in range(10)) #创建一个generator
	>>> G #generator
	<generator object <genexpr> at 0x02F3A8D0>

	# 打印generator, 如果要一个一个打印出来, 使用, 
	next()来得到generator的返回值
	>>> next(G)
	0
	>>> next(G)
	1
	>>> next(G)
	4

	# 没有更多的元素时，抛出StopIteration的错误。
	>>> next(g)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	StopIteration

	因为generator是可迭代对象, 所以可以使用for循环
	g = (x * x for x in range(10))
	>>> for i in g:
			print(i)

	
	0
	1
	4
	9
	16
	25
	36
	49
	64
	81

	斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
	1, 1, 2, 3, 5, 8, 13, 21, 34, ...

	>>> def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

	>>> fib(6)
	1
	1
	2
	3
	5
	8
	'done'

	注意，赋值语句：

	a, b = b, a + b
	相当于：

	t = (b, a + b) # t是一个tuple
	a = t[0]
	b = t[1]

	要把fib函数变成generator，只需要把print(b)改为yield b就可以了即：
		# 定义一个gengrator
		def fib(max):
	    n, a, b = 0, 0, 1
	    while n < max:
	        yield b
	        a, b = b, a + b
	        n = n + 1
	    return 'done'
	如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
		>>> def fib(max):
	    n, a, b = 0, 0, 1
	    while n < max:
	        yield b
	        a, b = b, a + b
	        n = n + 1
	    return 'done'

		>>> f = fib(6)
		>>> f
		<generator object fib at 0x02F3AA20>

    函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
    遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
	    >>> def odd():
		print('step 1')
		yield 1 #中断
		print('step 2') #执行
		yield(3)
		print('step 3')
		yield(5)

	调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
		>>> o = odd()
		>>> next(o)
		step 1
		1
		>>> next(o)
		step 2
		3
		>>> next(o)
		step 3
		5
		>>> next(o)
		Traceback (most recent call last):
		  File "<pyshell#36>", line 1, in <module>
		    next(o)
		StopIteration


	>>> for n in fib(3):
	print(n)

	
	1
	1
	2
	d
	o
	n
	e

	>>> g = fib(6)
	>>> while True:
		try:
			x = next(g)
			print('g:', x)
		except StopIteration as e:
			print('Generator return value:', e.value)
			break

		
	g: 1
	g: 1
	g: 2
	g: 3
	g: 5
	g: 8
	Generator return value: done

# 练习
	杨辉三角定义如下：

	          1
	         / \
	        1   1
	       / \ / \
	      1   2   1
	     / \ / \ / \
	    1   3   3   1
	   / \ / \ / \ / \
	  1   4   6   4   1
	 / \ / \ / \ / \ / \
	1   5   10  10  5   1
	把每一行看做一个list，试写一个generator，不断输出下一行的list：

	>>> def triangles(l):
	l = [1]
	while 1:
	    yield l
	    l = [1] + [ l[n] + l[n+1] for n in range(len(l)-1) ]  + [1]

	    
	>>> triangles(3)
	<generator object triangles at 0x02F51B10>

	>>> o = triangles(3)
	>>> next(o)
	[1]
	>>> next(o)
	[1, 1]
	>>> next(o)
	[1, 2, 1]
	>>> next(o)
	[1, 3, 3, 1]
	>>> next(o)
	[1, 4, 6, 4, 1]
	>>> next(o)
	[1, 5, 10, 10, 5, 1]
	>>> next(o)
	[1, 6, 15, 20, 15, 6, 1]

	请注意区分普通函数和generator函数，普通函数调用直接返回结果：
	>>> r = abs(6)
	>>> r
	6

	generator函数的“调用”实际返回一个generator对象：
	>>> g = fib(6)
	>>> g
	<generator object fib at 0x1022ef948>

迭代器
	可以直接作用于for循环的数据类型有以下几种
		一类是集合数据类型，如list、tuple、dict、set、str等
		一类是generator，包括生成器和带yield的generator function
	这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

	>>> from collections import Iterable
	>>> isinstance([], Iterable)
	True
	>>> isinstance({}, Iterable)
	True
	>>> isinstance('abc', Iterable)
	True
	>>> isinstance((x for x in range(6)), Iterable)
	True
	>>> isinstance(55, Iterable)
	False

	可以被, next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
	可以使用, isinstance()判断一个对象是否是Iterator对象
	>>> from collections import Iterator
	>>> isinstance([], Iterator) #isinstance() 判断一个对象是不是Iterator
	False
	>>> isinstance({}, Iterator)
	False
	>>> isinstance((x for x in range(6)), Iterator)
	True
	>>> isinstance('abc', Iterator)
	False

	生成器都是Iterator对象, 但list、dict、str虽然是Iterable，却不是Iterator
	把list、dict、str等Iterable变成Iterator可以使用, iter()函数：
	>>> isinstance(iter([]), Iterator)
	True
	>>> isinstance(iter('abc'), Iterator)
	True

	Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
	Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

	凡是可作用于for循环的对象都是Iterable类型
	凡是可作用于, next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
	集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
	Python的for循环本质上就是通过不断调用next()函数实现的
		for x in [1, 2, 3, 4, 5]:
	    	pass
	    
	    =

	    # 首先获得Iterator对象:
		x = iter([1, 2, 3, 4, 5])
		# 循环:
		while True:
		    try:
		        # 获得下一个值:
		        x = next(x)
		    except StopIteration:
		        # 遇到StopIteration就退出循环
		        break


# 廖雪峰,高级特性结束