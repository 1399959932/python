#!/usr/bin/python
# print('今天下午一点又一个面试但是坐地铁要连个小时还要多,所以被我推了')
# print('现在让我回顾一下昨天了解的高阶py函数')

map()		从新整理
	接受两个参数,一个为函数,另一个是可迭代对象
	map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
reduce()	累加运算
	reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数, 
	reduce把结果继续和序列的下一个元素做累积计算
	reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
filter()	过滤
	接受两个参数,一个为函数,另一个是序列
	filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


sorted		排序算法
	sorted()函数就可以对list进行排序
	>>> sorted([36, 44, 4, -1, 4, -250])
	[-250, -1, 4, 4, 36, 44]

	sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
	>>> sorted([36, 44, 4, -1, 4, -250], key=abs)
	[-1, 4, 4, 36, 44, -250]

	>>> sorted(['asd', 'tys', 'zss', 'Zzz'])
	['Zzz', 'asd', 'tys', 'zss']	#对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'

	>>> sorted(['asd', 'tys', 'zss', 'Zzz'], key=str.lower)	#key, 忽略大小写
	['asd', 'tys', 'zss', 'Zzz']

	>>> sorted(['asd', 'tys', 'zss', 'Zzz'], key=str.lower, reverse=True)
	['Zzz', 'zss', 'tys', 'asd']							#reverse=True, 反向排序

# 练习
	假设我们用一组tuple表示学生名字和成绩：
	L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
	请用sorted()对上述列表分别按名字排序：


	再按成绩从高到低排序:


# 返回函数
	高级函数除了可以接受函数作为参数外,也可以把函数作为结果值返回

	求和的函数
	>>> def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

	>>> calc_sum(6, 64, -99)
	-29

	可以不返回求和的结果，而是返回求和的函数：
	>>> def lazy_sum(*args):
		def sum():
			ax = 0
			for n in args:
				ax = ax + n
			return ax
		return sum

	>>> lazy_sum(6)	#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
	<function lazy_sum.<locals>.sum at 0x02F5E978>
	>>> f = lazy_sum(1, 2, 98, 6)	#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
	>>> f
	<function lazy_sum.<locals>.sum at 0x02F5E9C0>
	>>> f()
	107

	闭包:在函数lazy_sum中又定义了函数sum,内部函数sum可以引用外部函数lazy_sum的参数和局部变量
		当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包

	请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

	>>> f1 = lazy_sum(1, 3, 5, 7, 9)
	>>> f2 = lazy_sum(1, 3, 5, 7, 9)
	>>> f1==f2
	False
	f1()和f2()的调用结果互不影响。

闭包
	注意到返回的函数在其定义内部引用了局部变量args, 
		所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
		返回的函数并没有立刻执行，而是直到调用了f()才执行
	>>> def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs

	>>> f1, f2, f3 = count()
	>>> f1()
	9
	>>> f2()
	9
	>>> f3()

	全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
	!!!!##返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

	如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
	>>> def count():
			def f(j):
				def g():
					return j * j
				return g
			fs = []
			for i in range(1, 4):
				fs.append(f(i))
			return fs

	>>> f1, f2, f3 = count() #f1, f2, f3 = count([f(), f(), f()]) 
	>>> f1()
	1
	>>> f2()
	4
	>>> f3()
	9

# 练习
	利用闭包返回一个计数器函数，每次调用它返回递增整数：
	>>> def createCounter():
			n = 0
			def counter():
				nonlocal n
				n += 1
				return n
			return counter

	>>> createCounter
	<function createCounter at 0x02F5EBB8>
	>>> createCounter()
	<function createCounter.<locals>.counter at 0x02F5EB28>
	>>> f = createCounter()
	>>> f()
	1
	>>> f()
	2
	>>> f()
	3
# 小结
一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

匿名函数
	当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
	在Python中，对匿名函数提供了有限支持。还是以map()函数为例，\
	计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
	>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
	[1, 4, 9, 16, 25, 36, 49, 64, 81]

	SO, 

	lambda x: x * x  #关键字lambda表示匿名函数，冒号前面的x表示函数参数
	=
	def f(x):
		return x * x

	匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果


	用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
	>>> s = lambda x: x * x
	>>> s
	<function <lambda> at 0x02F5E9C0>
	>>> s(5)
	25

	同样，也可以把匿名函数作为返回值返回，比如：
	>>> def build(x, y):
    	return lambda: x * x + y * y


装饰器
	由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
	>>> def now():
	print('2018-03-15')

	
	>>> f = now
	>>> f()
	2018-03-15
	>>> now.__name__
	'now'
	>>> f.__name__
	'now'

	在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
	Decorator
		本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下:
		>>> def log(func):
			def wrapper(*args, **kw):
				print('call %s():' % func.__name__)
				return func(*args, **kw)
			return wrapper
		上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
		我们要借助Python的@语法，把decorator置于函数的定义处：

		本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
		>>> def log(func):
		def wrapper(*args, **kw):
			print('call %s():' % func.__name__)
			return func(*args, **kw)
		return wrapper

		# 上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
		>>> @log
		def now():
			print('2018-03-15')

		# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
		>>> now()
		call now():
		2018-03-15

		# 把@log放到now()函数的定义处，相当于执行了语句：
		now = log(now)

		由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
		于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。wrapper()函数的参数定义是(*args, **kw)，
		因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数

		# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，比如，要自定义log的文本：
		>>> def log(text):
		def decorator(func):
			def wrapper(*args, **kw):
				print('%s %s():' % (text, func.__name__))
				return func(*args, **kw)
			return wrapper
		return decorator

		# 这个3层嵌套的decorator用法如下
		>>> @log('execute')
		def now():
			print('2018-03-15')

		#执行结果
		>>> now()
		execute now():
		2018-03-15

		和两层嵌套的decorator相比，3层嵌套的效果是这样的：
		>>> now = log('execute')(now)

		!!!首先执行,log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数
		因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
		不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
		>>> import functools
		>>> def log(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('call %s():' % func.__name__)
				return func(*args, **kw)
			return wrapper

		或者针对带参数的decorator：
		>>> import functools
		>>> def log(text):
			def decorator(func):
				@functools.wraps(func)
				def wrapper(*args, **kw):
					print('%s %s():' % (text, func.__name__))
					return func(*rags, **kw)
				return wrapper
			return decorator

	import functools是导入functools模块
	#只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。

# 练习
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：


# 小结
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
http://blog.csdn.net/u013471155/article/details/68960244
关于函数“变量”（或“变量”函数）的理解
关于高阶函数的理解
关于嵌套函数的理解

	原则:
	1, 不能修改被装饰的函数的源代码
	2, 不能修改被装饰的函数的调用方式
	3, 满足1、2的情况下给程序增添功能
< 函数+实参高阶函数+返回值高阶函数+嵌套函数+语法糖 = 装饰器 >
	improt time
	>>> def test():
	    time.sleep(2)
	    print("test is running!")

	>>> test()	#等待约2秒后，输出
	test is running!

	# 升级一下
	import time
	>>> def test():
	    time.sleep(2)
	    print("test is running!")

	    
	>>> def deco(func):	#我们把test当作实参传递给形参func，即func=test
		start = time.time()
		func()	#注意，这里传递的是地址，也就是此时func也指向了之前test所定义的那个函数体，可以说在deco()内部，func就是test, 把函数名后面加上括号，就是对函数的调用（执行它）
		stop = time.time()
		print(stop - start)

		
	>>> deco(test)
	test is running!
	2.0121147632598877

	如果不修改调用方式，就是一定要有test()这条语句，那么就用到了第二种高阶函数，即返回值中包含函数名
	def deco(func):  
	    print(func)
	    return func 
		t = deco(test) #3

	嵌套函数指的是在函数内部定义一个函数，而不是调用，如：
		def func1():
		    def func2():
		        pass
		而不是
		def func1():
    		func2()

    想要统计程序运行时间，并且满足三原则

    3.真正的装饰器
    装饰器在装饰时，需要在每个函数前面加上
    test = timer(test)
    等价于
    @timer #语法糖

    4、装饰有参函数
    improt time

	def timer(func)
	    def deco(*args, **kwargs):  
	        start = time.time()
	        res = func(*args, **kwargs)
	        stop = time.time()
	        print(stop-start)
	        return res 
	    return deco

	@timer
	def test(parameter): #8
	    time.sleep(2)
	    print("test is running!")   
	    return "Returned value"
	test() 

	5、带参数的装饰器
	又增加了一个需求，一个装饰器，对不同的函数有不同的装饰。那么就需要知道对哪个函数采取哪种装饰。因此，就需要装饰器带一个参数来标记一下。例如：
	@decorator(parameter = value)

	比如有两个函数:
	def task1():
    time.sleep(2)
    print("in the task1")

	def task2():
    time.sleep(2)
    print("in the task2")

    要对这两个函数分别统计运行时间，但是要求统计之后输出：
	the task1/task2 run time is : 2.00……

	于是就要构造一个装饰器timer，并且需要告诉装饰器哪个是task1，哪个是task2，也就是要这样：
	@timer(parameter='task1') #
	def task1():
	    time.sleep(2)
	    print("in the task1")

	@timer(parameter='task2') #
	def task2():
	    time.sleep(2)
	    print("in the task2")

	那么方法有了，但是我们需要考虑如何把这个parameter参数传递到装饰器中，我们以往的装饰器，都是传递函数名字进去，而这次，多了一个参数，要怎么做呢？
	于是，就想到再加一层函数来接受参数，根据嵌套函数的概念，要想执行内函数，就要先执行外函数，才能调用到内函数，那么就有：
	def timer(parameter): #
    print("in the auth :", parameter)

    def outer_deco(func): #
        print("in the outer_wrapper:", parameter)

        def deco(*args, **kwargs):

        return deco

    return outer_deco
    首先timer(parameter)，接收参数parameter=’task1/2’，而@timer(parameter)也恰巧带了括号，那么就会执行这个函数， 那么就是相当于：
    timer = timer(parameter)
	task1 = timer(task1)

	SO
	import time

	def timer(parameter):

	    def outer_wrapper(func):

	        def wrapper(*args, **kwargs):
	            if parameter == 'task1':
	                start = time.time()
	                func(*args, **kwargs)
	                stop = time.time()
	                print("the task1 run time is :", stop - start)
	            elif parameter == 'task2':
	                start = time.time()
	                func(*args, **kwargs)
	                stop = time.time()
	                print("the task2 run time is :", stop - start)

	        return wrapper

	    return outer_wrapper

	@timer(parameter='task1')
	def task1():
	    time.sleep(2)
	    print("in the task1")

	@timer(parameter='task2')
	def task2():
	    time.sleep(2)
	    print("in the task2")

	>>> task1()
	in the task1
	the task1 run time is : 2.036116600036621
	>>> task2()
	in the task2
	the task2 run time is : 2.046116828918457



偏函数
	ython的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
	通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
	int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
	>>> int('32323')
	32323

	# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
	>>> int('32323', base=8)
	13523
	>>> int('32323', 16)
	205603

	# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
	>>> def int2(x, base=2):
	return int(x, base)

	>>> int2('1000000')
	64
	>>> int2('10000001')
	129

	# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
	>>> import functools
	>>> int2 = functools.partial(int, base=2)
	>>> int2('1000000')
	64
	>>> int2('1010101')
	# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，

	注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
	>>> int2('1000000', base=10)
	1000000

	最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
	int2 = functools.partial(int, base=2)
	实际上固定了int()函数的关键字参数base，也就是：

	int2('10010')
	相当于：

	kw = { 'base': 2 }
	int('10010', **kw)

	当传入：
	max2 = functools.partial(max, 10)
	实际上会把10作为*args的一部分自动加到左边，也就是：

	max2(5, 6, 7)
	相当于：

	args = (10, 5, 6, 7)
	max(*args)
	10

	# 实例:
	>>> max2 = functools.partial(max, 10)
	>>> max(args)
	6
	>>> args
	(6, 5, 3)
	>>> max2(args)
	Traceback (most recent call last):
	  File "<pyshell#293>", line 1, in <module>
	    max2(args)
	TypeError: '>' not supported between instances of 'tuple' and 'int'
	>>> max2(*args)
	10

# 小结
	当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
	functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值）
