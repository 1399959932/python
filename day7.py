#!use/bin/python
# print('hello, world')

# 函数
# 	def func():
# 	求和符号∑

# 求圆的面积
	# import math # 导入math模块，下面用到pi
	# list1 = [12.34, 9.08, 73.1] # 将3个不同面积的圆半径定义成一个lis

	# def area_sum(i): # 定义area_sum函数，套用圆的面积计算公式
	# 	area = math.pi * i * i
	# 	print(area) # 打印圆的面积

	# for iii in list1:# 将列表的3个半径循环
	# 	print(iii)  # 一次将值给area_sum函数

	# area_sum(list1[2]) #求圆的面积

# python内置函数
	abs()	只有一个参数,求其绝对值
		def my_abs(x):
	    if x >= 0:
	        return x
	    else:
	        return -x
	hex(i)	把一个整数转换成十六进制表示的字符串

# 调用函数:
	# 把函数赋值给一个变量
		a = abs # 变量a指向abs函数
		a(-1) # 所以也可以通过a调用abs函数
	# 直接调用:
		abs(i) #函数名传参

# 简洁并符合要求是第一生产力
	n1 = hex(n1)
	n2 = hex(n2)
	print(str(n1), str(n2))

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。

如果你已经把 my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：

	# 如果想定义一个什么事也不做的空函数，可以用pass语句：
		def nop():
			pass
	# pass可以用来作为占位符,pass也可以用在其他语句里
		if age = 18:
			pass
	# 缺少了pass，代码运行就会有语法错误

# 参数检查

	# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出
		TypeError：
	# 但是如果参数类型不对，Python解释器就无法帮我们检查

	改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。
		数据类型检查可以用内置函数	isinstance()实现：
	def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
return	# 可以随时返回函数结果
		# 执行完毕也没有return语句时，自动return None

# 函数返回多个值: 其实就是一个tuple()

# 游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，
# 就可以计算出新的新的坐标
	import math # import math语句表示导入math包,
	 			# 并允许后续代码引用math包里的sin、cos等函数

	def move(x, y, step, angle=0):
	    nx = x + step * math.cos(angle)
	    ny = y - step * math.sin(angle)
	    return nx, ny

	x, y = move(100, 100, 60, math.pi / 6)
	print(x, y)
	151.96152422706632 70.0 # 返回值(但是这是一种假象,python返回的仍然是但一值)
	r = move(100, 100, 60, math.pi / 6)
	print(r)
	(151.96152422706632, 70.0) # 返回值是一个tuple
	# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
	# 按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便

# 练习

请定义一个函数 quadratic(a, b, c)，接收3个参数，返回'一元二次'方程：
axx + bx + c = 0 的两个解。△ = (bb-4ac)

	import math
	def quadratic(a, b, c): # quadratic ~ 二次方程式
		d = b*b-4*a*c
		if d < 0:
		    print('此方程无解')
		elif d == 0:
		    x=b/((-2)*a)
		else:
		    x1 = (-b + math.sqrt(d))/2/a
		    x2 = (-b + math.sqrt(d))/2/a
		    return x1,x2

# 位置参数
	# 计算x2的函数
		def power(x): # 对于power(x)函数，参数x就是一个位置参数。
			return x * x 	
	#当我们调用power函数时，必须传入有且仅有的一个参数x

	# power(x, n)函数，可以计算x任意n次方
		def power(x, n):
	    s = 1
	    while n > 0:
	        n = n - 1
	        s = s * x
	    return s

# 默认参数
	1.是必选参数在前，默认参数在后
	2.如何设置默认参数:/	当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
		变化小的参数就可以作为默认参数。
	def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    # 当我们要计算x*x时就直接 power(x)就可以,但需要计算2次方以上的时候,
    # 需要传入两个参数几 power(x, n)

    def enroll(name,gender,age=6,city='beijing'):
		print('name:', name)
		print('gender:', gender)
		print('age:', age)
		print('city:', city
	这样,大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：		
	>>>enroll('Sarah', 'F')  # 也可以提供2~4个参数
	name: Sarah
	gender: F
	age: 6
	city: beijing
	enroll('Adam', 'M', city='Tianjin') # 也可以不按默认顺序提供参数,
										# 但需要指定指定其参数名

	# 默认参数有个最大的坑:即
	def add_end(L=[]):
	    L.append('END')
	    return L
	>>>app_end() # 第一次调用,没问题['EDN']
	# BUT
	>>>app_end() # 再次调用时['END', 'END']
	>>>app_end() # 再次调用时['END', 'END', 'END']
	# Because
	# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
	# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
!!!!SO:定义默认参数要牢记一点：默认参数必须指向不变对象！

	# 要修改上面的例子，我们可以用None这个不变对象来实现
	def add_end(L=None):
	    if L is None:
	        L = []
	    L.append('END')
	    return L

# 可变参数
	# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……
	def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

    >>>calc([1, 2, 3]) # 但是调用的时候，需要先组装出一个list或tuple


    >>>calc(1, 2, 3) # 所以但我们想直接需要使用可变参数,即:
    def calc(*numbers): # 多加了个*
    sum = 0		#在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
    for n in numbers:	
        sum = sum + n * n
    return sum
    # 可以传入任意个参数，包括0个参数


    # 如果已经有一个list或者tuple，要调用一个可变参数
    >>> nums = [1, 2, 3]
	>>> calc(nums[0], nums[1], nums[2])
	# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
	>>>calc(*nums)

# 关键词参数
	def person(name, age, **kw):
    	print('name:', name, 'age:', age, 'other:', kw)
    # 函数person除了必选参数name和age外，还接受关键字参数kw。
    # 在调用该函数时，可以只传入必选参数：
    # 也可以传入任意个数的关键字参数
    >>> person('Jack', 24, city=extra['city'], job=extra['job'])
    # 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
    >>>extra = {'city': 'Beijing', 'job': 'Engineer'}
    >>>person('Jack', 24, **extra)
    # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
    # 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
	
# 命名关键字参数
	# 检查是否有city和job参数
	def person(name, age, **kw):
	    if 'city' in kw:
	        # 有city参数
	        pass
	    if 'job' in kw:
	        # 有job参数
	        pass
	    print('name:', name, 'age:', age, 'other:', kw)
	# 调用者仍可以传入不受限制的关键字参数：
	>>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
	# 如果要限制关键字参数的名字，就可以用命名关键字参数
	# 例:只接受city和job的参数
	def person(name, age, *, city, job): #和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，

    	print(name, age, city, job)
	# *后面的参数被视为命名关键字参数
	>>> person('Jack', 24, city='Beijing', job='Engineer')
	
	# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
	def person(name, age, *args, city, job):
    	print(name, age, args, city, job)
    # 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错

    # 命名关键字参数可以有缺省值，从而简化调用
    def person(name, age, *, city='Beijing', job):
    	print(name, age, city, job)

# 参数组合
	# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
	# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
	def f1(a, b, c=0, *args, **kw):
    	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    >>> f1(1, 2, 3, 'a', 'b', x=99)

	def f2(a, b, c=0, *, d, **kw):
    	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    >>> f2(1, 2, d=99, ext=None)

    # 还可以通过一个tuple和dict，调用上述函数,即:
    >>> args = (1, 2, 3, 4)
	>>> kw = {'d': 99, 'x': '#'}
	>>> f1(*args, **kw)
	a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
	>>> args = (1, 2, 3)
	>>> kw = {'d': 88, 'x': '#'}
	>>> f2(*args, **kw)
	a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

	*args是可变参数，args接收的是一个tuple；
	**kw是关键字参数，kw接收的是一个dict

	# SO,对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
	# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差

# 练习

	# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
	# def product(x, y):
 	# return x * y

 	index1:
	    def product(a):
	    c = 1
	    if  isinstance(a,(int,float)):
	        print(a)
	    else:
	     if a is ():
	        raise TypeError('leixingbudui')
	        return 'wrong'
	     for b in a:
	         c = c * b
	     print(c)

	index2:
	def product(x, y=1,*args):
	    sum=1
	    sum=x*y
	    for n in args:
	        sum=sum*n
	    return sum

# 递归函数	// 如果一个函数在内部调用自身本身，这个函数就是递归函数
	# 在函数内部，可以调用其他函数。
	# 阶乘 fact(n)的递归写法
	def fact(n):
	    if n==1:
	        return 1
	    return n * fact(n - 1)

	# 递归函数的优点是定义简单，逻辑清晰
	# 使用递归函数需要注意防止栈溢出

	在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
	栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧
	由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试
	fact(1000)：
	RuntimeError: maximum recursion depth exceeded in comparison
	解决递归调用栈溢出的方法是通过尾递归优化,事实上尾递归和循环的效果是一样的，所以
	把循环看成是一种特殊的尾递归函数也是可以的

	尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
	这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况


	要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中
	def fact(n):
    	return fact_iter(n, 1)

	def fact_iter(num, product):
	    if num == 1:
	        return product
	    return fact_iter(num - 1, num * product)

	SyntaxError: invalid syntax / 无效语法,语法错误

练习

	汉诺塔的移动可以用递归函数非常简单地实现。

	# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
	# 然后打印出把所有盘子从A借助B移动到C的方法，例如：

    # if n == 1:
    # print(a, '-->', c)

参数:
	# 形参,实参
	形参:函数创建,定义过程中的name是形参,/paramter
	实参:函数在调用过程中传进去的/argument

	name'.__doc__'   打印函数文档


关键词参数
	der person(,):不用按照位置,可以指定关键字赋值给指定参数,不用考虑位置即name= '',

默认参数
	der person(,): name='陈老爷'

收集参数
	der person(*name): *name ,给他一个形参,tuple()形式的


