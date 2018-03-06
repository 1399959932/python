#!usr/bin/python
# 有返回值的是函数 没有返回值的是过程,而python只有函数,没有过程
	def back():
		return [1, 'hello', 3.145]
# ,可以被看成元祖
	def back():
		return 1, 'hello', 3.145

# 局部变量(Loval Variable)
	在函数内部定义的参数,是局部变量,只能在函数内部使用


# 全局变量(Global Variable)
	在python中可以随便访问全局变量,但不能在函数内部修改全局变量,
如果修改的话,python内部会创建一个相同name的局部变量来代替
	# 如果想修改全局变量
	count = 5
	def func():
		global count
		count = 10
		print(10)
	>>>myfun() #10
	>>>print(count) #10

# 内嵌函数
	def fun1():
		print(',')
		def fun2():
			print(1)
		fun2()
	# fun2()是在,fun1()内部声明的,所以只能在.fun1()内部使用
	# fun2()是不能再外部调用的

# 闭包
	def funx(x):
		def funy(y):
			return x * y
		return funy
	我们可以说,funy()就是,funx()的闭包

# lambda 语句
	def ds(x):
	return 2 * x + 1
	=
	lambda x : 2 * x + 1
	>>>name = lambda x : 2 * x + 1 #调用
	>>>name(i)

	# SO
	add(3, 4)
	=
	lambda x, y : x + y

# filter(abject)  #过滤器
	filter(func()/None,[]) #返回值可用list()修饰 例:
	# 过滤1到10的奇数
	def odd(x):
		return x % 2

	>>> temp = range(10)
	>>> show = filter(odd, temp)
	>>> list(show)
	[1, 3, 5, 7, 9]

	=

	list(filter(lambda x : x % 2, range(10)))

# map() #映射
	list(map(lambda x : x * 2, range(10)))
	>>>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]




