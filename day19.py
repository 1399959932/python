#!/usr/bin/python
print('最近这几天感觉有点对python过分重视然后, 把看家本领php忘记了')
print('今天的目标是吧这个木块结束, 然后看一下php')

# 定制类
	__str__
	# 如果我们定义一个类：
	>>> class Student(object):
	...     def __init__(self, name):
	...         self.name = name
	...

	>>> print(Student('Michael'))	#打印
	<__main__.Student object at 0x109afb190>
	# 打印字符串处理
	>>> class Studnet(object):	#student名字错了
		def __init__(self, name):
			self.name = name
		def __str__(self):
			return 'Student onject (name: %s)' % self.name

		
	>>> print(Stunder('Ronin Chen'))	#student名字错了
	Traceback (most recent call last):
	  File "<pyshell#13>", line 1, in <module>
	    print(Stunder('Ronin Chen'))
	NameError: name 'Stunder' is not defined
	>>> print(Studnet('Ronin Chen'))
	Student onject (name: Ronin Chen)



	>>> s = Student('Chen')
	>>> s
	<__main__.Student object at 0x02F74850>
	这是因为直接显示变量调用的不是, __str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
	解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的, SO
		>>> class Student(object):
				def __init__(self, name):
					self.name = name
				def __str__(self):
					return 'Student object (name=%s)' % self.name
				__repr__ = __str__

				
			>>> s = Student('Chen')
			>>> s
		Student object (name=Chen)

__iter__  #循环
	如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
	该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
	# SO,
		class Fib(object):
	    def __init__(self):
	        self.a, self.b = 0, 1 # 初始化两个计数器a，b

	    def __iter__(self):
	        return self # 实例本身就是迭代对象，故返回自己

	    def __next__(self):
	        self.a, self.b = self.b, self.a + self.b # 计算下一个值
	        if self.a > 100000: # 退出循环的条件
	            raise StopIteration()
	        return self.a # 返回下一个值
	现在，试试把Fib实例作用于for循环：

	>>> for n in Fib():
	...     print(n)
	...
	1
	1
	2
	3
	5
	...
	46368
	75025

__getitem__ 
	#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
	>>> Fib()
	<__main__.Fib object at 0x02F85790>
	>>> Fib()[6]
	Traceback (most recent call last):
	  File "<pyshell#50>", line 1, in <module>
	    Fib()[6]
	TypeError: 'Fib' object does not support indexing

	要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
	>>> class Fib(object):
		def __getitem__(self, n):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a

		
	>>> f = Fib()
	>>> f[0]
	1
	>>> f[1]
	1
	>>> f[2]
	2
	>>> f[3]
	3
	>>> f[4]
	5
	>>> f[5]
	8
	>>> f[6]
	13

	# list有个神奇的切片方法：
	>>> list(range(100))[3:6]
	[3, 4, 5]
	>>> Fib(range(100))[3:6]
	Traceback (most recent call last):
	  File "<pyshell#79>", line 1, in <module>
	    Fib(range(100))[3:6]
	TypeError: object() takes no parameters
	对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
	
	>>> class Fib(object):
	    def __getitem__(self, n):
	        if isinstance(n, int): # n是索引
	            a, b = 1, 1
	            for x in range(n):
	                a, b = b, a + b
	            return a
	        if isinstance(n, slice): # n是切片
	            start = n.start
	            stop = n.stop
	            if start is None:
	                start = 0
	            a, b = 1, 1
	            L = []
	            for x in range(stop):
	                if x >= start:
	                    L.append(a)
	                a, b = b, a + b
	            return L

	        
	>>> f = Fib()
	>>> f[0:6]
	[1, 1, 2, 3, 5, 8]
	>>> f[:6]
	[1, 1, 2, 3, 5, 8]
	>>> f[:10:2]
	[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

__getattr__	#动态返回一个属性
	# 例：
	>>> class Student(object):
		def __init__(self):
			self.name = 'Ronin Chen'

			
	>>> s = Student()
	>>> s.name
	'Ronin Chen'
	>>> print(s.name)
	Ronin Chen
	>>> print(s.sorce)
	Traceback (most recent call last):
	  File "<pyshell#15>", line 1, in <module>
	    print(s.sorce)
	AttributeError: 'Student' object has no attribute 'sorce'

	用完全动态的__getattr__，我们可以写出一个链式调用：
	>>> class Chain(object):

	    def __init__(self, path=''):
	        self._path = path

	    def __getattr__(self, path):
	        return Chain('%s/%s' % (self._path, path))

	    def __str__(self):
	        return self._path

	    __repr__ = __str__

	    
	>>> Chain().status.user.timeline.list
	/status/user/timeline/list

__call__	#只需要定义一个__call__()方法，就可以直接对实例进行调用
	>>> class Student(object):
		def __init__(self, name):
			self.name = name
		def __call__(self):
			print('My name is %s.' % self.name)

			
	>>> s = Student()	#没参
	Traceback (most recent call last):
	  File "<pyshell#72>", line 1, in <module>
	    s = Student()
	TypeError: __init__() missing 1 required positional argument: 'name'
	>>> s = Student('Ronin Chen')
	>>> s()
	My name is Ronin Chen.
	>>> 

	通过, callable()函数，我们就可以判断一个对象是否是“可调用”对象
	>>> callable(s())
	My name is Ronin Chen.
	False
	>>> callable(s)
	True
	>>> callable('str')
	False

小结
	Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。


使用枚举类
	当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份
		#好处是简单，缺点是类型是int，并且仍然是变量
		JAN = 1
		FEB = 2
		MAR = 3
		...
		NOV = 11
		DEC = 12

	更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
	>>> from enum import Enum
	>>> Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	>>> for name, member in Month.__members__.items():	#我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
		print(name, '=>', member, ',', member.value)

		
	Jan => Month.Jan , 1
	Feb => Month.Feb , 2
	Mar => Month.Mar , 3
	Apr => Month.Apr , 4
	May => Month.May , 5
	Jun => Month.Jun , 6
	Jul => Month.Jul , 7
	Aug => Month.Aug , 8
	Sep => Month.Sep , 9
	Oct => Month.Oct , 10
	Nov => Month.Nov , 11
	Dec => Month.Dec , 12

	# value属性则是自动赋给成员的int常量，默认从1开始计数。
	# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
	>>> from enum import Enum, unique
	>>> @unique	#@unique装饰器可以帮助我们检查保证没有重复值。
	class Weekday(Enum):
		Sun = 0	# Sun的value被设定为0
		Mon = 1
		Tue = 2
		Web = 3
		Thu = 4
		Fri = 5
		Sat = 6

	# 访问这些枚举类型可以有若干种方法：
	>>> day1 = Weekday.Mon
	>>> print(day1)
	Weekday.Mon
	>>> print(Weekday.Tue)
	Weekday.Tue
	>>> print(Weekday['Tue'])
	Weekday.Tue
	>>> print(Weekday.Tue.value)
	2
	>>> print(day1 == Weekday.Mon)
	True
	>>> print(day1 == Weekday.Tue)
	False
	>>> print(Weekday(1))
	Weekday.Mon
	>>> print(day1 == Weekday(1))
	True
	>>> Weekday(7)
	Traceback (most recent call last):
	  ...
	ValueError: 7 is not a valid Weekday
	>>> for name, member in Weekday.__members__.items():
	...     print(name, '=>', member)
	...
	Sun => Weekday.Sun
	Mon => Weekday.Mon
	Tue => Weekday.Tue
	Wed => Weekday.Wed
	Thu => Weekday.Thu
	Fri => Weekday.Fri
	Sat => Weekday.Sat

使用元类
	type()函数可以查看一个类型或变量的类型
	动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
	class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

    >>> from hello import Hello #我失败了, 建了hello.py文件但是
	 	# from hello import Hello
		# Traceback (most recent call last):
		#   File "<pyshell#132>", line 1, in <module>
		#     from hello import Hello
		# ModuleNotFoundError: No module named 'hello'
	>>> h = Hello()
	>>> h.hello()
	Hello, world.
	>>> print(type(Hello))	#Hello是一个class，它的类型就是type
	<class 'type'>
	>>> print(type(h))	#而h是一个实例，它的类型就是class Hello
	<class 'hello.Hello'>


	我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
	type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
	
	>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
	>>> h = Hello()
	>>> h.hello()
	Hello, world.
	>>> print(type(Hello))
	<class 'type'>
	>>> print(type(h))
	<class '__main__.Hello'>

	要创建一个class对象，type()函数依次传入3个参数：
	1.class的名称；
	2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
	3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
	#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class

metaclass
	metaclass，直译为元类，简单的解释就是：
	当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
	但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
	连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
	所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”

	# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：	
	# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

	
小结
metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心	