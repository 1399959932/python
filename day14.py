#!usr/bin/python
# print('今天是day14,面试了两家')
函数式编程
	函数就是面向过程的程序设计的基本单元
	函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

	>>> abs
	<built-in function abs>
	>>> abs(55)
	55
	>>> a = abs
	>>> a
	<built-in function abs>
	>>> a = abs(5)
	>>> 
	>>> a
	>>> a
	5
	>>> 
	函数本身也可以赋值给变量,变量可以指向函数

	>>> f = abs
	>>> f(6)
	6
	说明变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。

	>>> abs = 10
	>>> abs(10)
	Traceback (most recent call last):
	  File "<pyshell#35>", line 1, in <module>
	    abs(10)
	TypeError: 'int' object is not callable
	由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，
	要用import builtins; builtins.abs = 10

	>>> def add(x, y, z):	# x = -5, y = 6, f = abs
	return f(x) + f(y)

	>>> add(-5, 6, abs)		#f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
	11

高阶函数:
	map(), :
		map()函数接收两个参数，一个是函数，一个是Iterable(可迭代对象)
		map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
		>>> def f(x):
		return x * x

	>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
	>>> list(r)
	[1, 4, 9, 16, 25, 36, 49, 64, 81]

	# 循环写法
	>>> l = []
	>>> for i in[1, 2, 3, 4, 5, 6, 7, 8]:
		l.append(f(i))

		
	>>> l
	[1, 4, 9, 16, 25, 36, 49, 64]

	reduce(), :
		reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数, 
		reduce把结果继续和序列的下一个元素做累积计算, 即
		>>> reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

		对一个序列求和，就可以用reduce, 当然求和运算可以直接用Python内建函数, sum()，没必要动用reduce
		>>> from functools import reduce
		>>> def add(x, y):
			return x + y

		>>> reduce(add, [1, 2, 3, 4, 5, 6])
		21

		但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
		>>> from functools import reduce
		>>> def ff(x, y):
			return x * 10 + y

		>>> reduce(ff, [1, 2, 3, 4, 5, 6])
		123456

		考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
		>>> from functools import reduce
		>>> def ff(x, y):
			return x * 10 + y

		>>> def char2num(s):
			digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
			return digits[s]

		>>> reduce(ff ,map(char2num, '155523232'))
		155523232

		整理成一个str2int的函数就是;
		>>> from functools import reduce
		>>> DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		>>> def str2int(s):
			def fn(x, y):
				return x * 10 + y
			def char2num(s):
				return DIGITS[s]
			return reduce(fn, map(char2num, s))

		>>> str2int('65656')
		65656

		还可以用lambda函数进一步简化成：
		>>> from functools import reduce
		>>> DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		>>> def char2num(s):
			return DIGITS[s]

		>>> def str2int(s):
			return reduce(lambda x, y : x * 10 + y, map(char2num, s))

		>>> str2int('5666')
		5666

	filter()
		filter()函数用于过滤序列。和map()类似,接收一个函数和一个序列, 
		和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

		在一个list中，删掉偶数，只保留奇数，可以这么写：
		>>> def is_odd(n):
			return n % 2 == 1

		>>> list(filter(is_odd, [1, 2, 3, 4, 5]))
		[1, 3, 5]

		序列中的空字符串删掉，可以这么写：
		>>> def not_empty(s):
			return s and s.strip()

		>>> list(filter(not_empty, ['S', '', '', None, 'SS']))
		['S', 'SS']

		filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
		返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

		用filter求素数
			用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
			def _odd_iter(): 		#这是一个生成器，并且是一个无限序列
			    n = 1
			    while True:
			        n = n + 2
			        yield n

			

			def _not_divisible(n): 	#定义一个筛选函数：
			    return lambda x: x % n > 0
		

			def primes():			#定义一个生成器，不断返回下一个素数：
			    yield 2
			    it = _odd_iter() 	# 初始序列
			    while True:
			        n = next(it) 	# 返回序列的第一个数
			        yield n
			        it = filter(_not_divisible(n), it) # 构造新序列
			这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

			由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

			# 打印1000以内的素数:
			for n in primes():
			    if n < 1000:
			        print(n)
			    else:
			        break
			注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

练习
	回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：	
	def is_palindrome(n):
    return str(n) == str(n)[::-1]

    >>>(再议)