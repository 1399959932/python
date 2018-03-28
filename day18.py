#!usr/bin/python
面向对象高级编程
	在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
	我们会讨论多重继承、定制类、元类等概念

使用__slots__
	正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
	class Student(object):
	    pass

	然后，尝试给实例绑定一个属性：

	>>> s = Student()
	>>> s.name = 'Michael' # 动态给实例绑定一个属性
	>>> print(s.name)
	Michael
	还可以尝试给实例绑定一个方法：

	>>> def set_age(self, age): # 定义一个函数作为实例方法
	...     self.age = age
	...
	>>> from types import MethodType
	>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
	>>> s.set_age(25) # 调用实例方法
	>>> s.age # 测试结果
	25
	但是，给一个实例绑定的方法，对另一个实例是不起作用的：

	>>> s2 = Student() # 创建新的实例
	>>> s2.set_age(25) # 尝试调用方法
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'Student' object has no attribute 'set_age'
	为了给所有实例都绑定方法，可以给class绑定方法：

	>>> def set_score(self, score):
	...     self.score = score
	...
	>>> Student.set_score = set_score
	给class绑定方法后，所有实例均可调用：

	>>> s.set_score(100)
	>>> s.score
	100
	>>> s2.set_score(99)
	>>> s2.score
	99
	通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。


使用__slots__
	为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
	比如，只允许对Student实例添加name和age属性
	>>> class Student(object):
		__slots__ = ('name', 'age')

	>>> c = Student()
	>>> c.name = 'Ronin Chen'
	>>> c.age = 16
	>>> c.score = 99	#__slots__没有'score'属性, 试图绑定score将得到AttributeError的错误
	Traceback (most recent call last):
	  File "<pyshell#37>", line 1, in <module>
	    c.score = 99
	AttributeError: 'Student' object has no attribute 'score'

	使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
	>>> class GS(Student):
		pass

	>>> g = GS()	
	>>> g.score = 999	#没有报错, 继承的'Student'并没有__slots__

使用@property
	在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
	>>> class Student(object):
		pass

	>>> s = Student()
	>>> s.score = 999

	这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
	>>> class Student(object):
		def get_score(self):
			return self._score
		def set_score(self, value):
			if not isinstance(value, int):
				raise ValueError('score must be an int')
			if value < 0 or value > 100:
				raise ValueError('score must between 0~100')
			self._score = value

			
	>>> s = Student()
	>>> s.set_score(66)
	>>> s.get_score()
	66
	>>> s.set_score(666)
	Traceback (most recent call last):
	  File "<pyshell#76>", line 1, in <module>
	    s.set_score(666)
	  File "<pyshell#72>", line 8, in set_score
	    raise ValueError('score must between 0~100')
	ValueError: score must between 0~100

	Python内置的@property装饰器就是负责把一个方法变成属性调用的

	下面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
	class Student(object):

    @property 	#被装饰的
    def birth(self):
        return self._birth

    @birth.setter	#装饰'birth', 使其可写入
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 练习
	请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
    >>> class Screen(object):
	    @property
	    def Width(self):
	        return self._Width
	    @Width.setter
	    def Width(self, w_value):
	        self._Width = w_value
	    @property
	    def Height(self):
	        return self._Height
	    @Height.setter
	    def Height(self, h_value):
	        self._Height = h_value
	    @property
	    def Resolution(self):
	        return self._Width * self._Height

	>>> s = Screen()
	>>> s.Width = 6
	>>> s.Width
	6
	>>> s.Height = 6
	>>> s.Height
	6
	>>> s.Resolution
	36


多重继承
	继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能
	class Dog(Mammal, Runnable):	#可以继承多个类
    pass
	
MixIn