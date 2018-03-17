#!/usr/bin/python
print('今天很神奇下雪了,而且我洗漱吃饭回来两点了个der')

类和实例
	类是抽象的模板
	而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同

类
	定义类是通过class关键字
	class Student(object):
		pass
	class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
	
	定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
	>>> bart = Student
	>>> bart
	<class '__main__.Student'>
	>>> bart = Student()
	>>> bart
	<__main__.Student object at 0x0048AC30> #后面的0x10a67a590是内存地址，每个object的地址都不一样
	>>> Student 	#Student本身则是一个类
	<class '__main__.Student'>

	>>> bart.name = 'Ronin Chen'
	>>> bart.name
	'Ronin Chen'

	由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，
	在创建实例的时候，就把name，score等属性绑上去：
	>>> class Student(object):
		def __init__(self, name, score):	#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
			self.name = name
			self.score = score

		
	>>> bart = Student('Bart Simpson')	#有了__init__方法，在创建实例的时候，就不能传入空的参数了，
	  File "<pyshell#20>", line 1, in <module>
	    bart = Student('Bart Simpson')
	TypeError: __init__() missing 1 required positional argument: 'score'
	>>> bart = Student('Ronin Chen', 99)	#必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
	>>> bart.name
	'Ronin Chen'
	>>> bart.score
	99

	!!!和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

# 数据封装
	面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的成绩：
	>>> class Student(object):
		pass

	>>> Student
	<class '__main__.Student'>
	>>> print(Student)
	<class '__main__.Student'>
	>>> print('Student')
	Student
	>>> bart = Student()
	>>> bart
	<__main__.Student object at 0x02F37F50>
	>>> Student
	<class '__main__.Student'>
	>>> bart.name = 'Ronin Chen'
	>>> bart.name
	'Ronin Chen'
	>>> class Student(object):
		def __init__(self, name, score):
			self.name = name
			self.score = score

			
	>>> bart = Student('陈', 66)
	>>> bart.name
	'陈'
	>>> bart.score
	66
	>>> def print_score(std):
		print('%s: %s' % (std.name, std.score))

		
	>>> print_score(bart)
	陈: 66
	>>> class Student(object):

	    def __init__(self, name, score):
	        self.name = name
	        self.score = score

	    def print_score(self):
	        print('%s: %s' % (self.name, self.score))

	        
	>>> bart.print_score()	#这个地方怎么会报错呢,是我没有安装那个pip第三包函数宝的问题么
	Traceback (most recent call last):
	  File "<pyshell#112>", line 1, in <module>
	    bart.print_score()
	AttributeError: 'Student' object has no attribute 'print_score'


# 小结
	类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
	方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
	通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
	和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
	>>> bart = Student('CHEN', 66)
	>>> lisa = Student('chen', 88)
	>>> bart.age = 8
	>>> bart.age
	8
	>>> lisa.age
	Traceback (most rece
		nt call last):
	  File "<pyshell#131>", line 1, in <module>
	    lisa.age
	AttributeError: 'Student' object has no attribute 'age'

访问限制
	在Class内部，可以有属性和方法'函数'，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
	但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：
	>>> bart = Student('陈', 66)
	>>> bart.score
	66
	>>> bart.score = 99
	>>> bart.score
	99

	如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，
	所以，我们把Student类改一改：
	>>> class Student(object):
		def __init__(self, name, score):
			self.__name = name
			self.__score =  score

			
	>>> class Student(object):
		def __init__(self, name, score):
			self.__name = name
			self.__score =  score
		def print_score(self):
			print('%s: %s' % (self.__name, self.__score))

	对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：		
	>>> bart = Student('SSSS', 55)
	>>> bart.__name
	Traceback (most recent call last):
	  File "<pyshell#149>", line 1, in <module>
	    bart.__name
	AttributeError: 'Student' object has no attribute '__name'

	这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
	但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
	class Student(object):
	    ...

	    def get_name(self):
	        return self.__name

	    def get_score(self):
	        return self.__score

	如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
	class Student(object):
	    ...

	    def set_score(self, score):
	        self.__score = score

	你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
	class Student(object):
	    ...

	    def set_score(self, score):
	        if 0 <= score <= 100:
	            self.__score = score
	        else:
	            raise ValueError('bad score')

	在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
	不是private变量，所以，不能用__name__、__score__这样的变量名

	_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”

	双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
	>>> bart._Student__name
	'SSSS'

	但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
	总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

	最后注意下面的这种错误写法：
	>>> bart = Student('Bart Simpson', 59)
	>>> bart.get_name()
	'Bart Simpson'
	>>> bart.__name = 'New Name' # 设置__name变量！
	>>> bart.__name
	'New Name'
	表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

	>>> bart.get_name() # get_name()内部返回self.__name
	'Bart Simpson'

	This is '源代码'
		#!/usr/bin/env python3
		# -*- coding: utf-8 -*-

		class Student(object):

		    def __init__(self, name, score):
		        self.__name = name
		        self.__score = score

		    def get_name(self):
		        return self.__name

		    def get_score(self):
		        return self.__score

		    def set_score(self, score):
		        if 0 <= score <= 100:
		            self.__score = score
		        else:
		            raise ValueError('bad score')

		    def get_grade(self):
		        if self.__score >= 90:
		            return 'A'
		        elif self.__score >= 60:
		            return 'B'
		        else:
		            return 'C'

		bart = Student('Bart Simpson', 59)
		print('bart.get_name() =', bart.get_name())
		bart.set_score(60)
		print('bart.get_score() =', bart.get_score())

		print('DO NOT use bart._Student__name:', bart._Student__name)

继承和多态
	在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）

	比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
	>>> Animal()	
	<__main__.Animal object at 0x02F37CF0>
	>>> print(Animal())
	<__main__.Animal object at 0x02F37BD0>
	>>> class Dog(Animal):	#对于Dog来说，Animal就是它的父类
		pass

	>>> 
	>>> class Cat(Animal):
		pass

	>>> dog.run()
	Animal is running
	>>> cat.run()
	Animal is running

	对于Animal来说，Dog就是它的子类。Cat和Dog类似
	>>> class Dog(Animal):
		def run(self):
			print('Dog is running...')
		def eat(self):
			print('Eating meat')

			
	>>> class Dog(Animal):
		def run(self):
			print('Dog is running...')
		def eat(self):
			print('Eating meat')

			
	>>> class Cat(Animal):
		def run(self):
			print('Cat is running.')

			
	>>> Cat()
	<__main__.Cat object at 0x02F37AB0>
	>>> dog = Dog()
	>>> dog.run()
	Dog is running...
	>>> cat = Cat()
	>>> cat
	<__main__.Cat object at 0x02F37690>
	>>> cat.run()
	Cat is running.
	>>> dog.eat()
	Eating meat

	当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，
	总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态

	当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
		a = list() # a是list类型
		b = Animal() # b是Animal类型
		c = Dog() # c是Dog类型

	判断一个变量是否是某个类型可以用, isinstance()判断：

	>>> isinstance(a, list)
	True
	>>> isinstance(b, Animal)
	True
	>>> isinstance(c, Dog)
	True
	>>> isinstance(c, Animal)
	True
	所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：

	>>> b = Animal()
	>>> isinstance(b, Dog)
	False
	Dog可以看成Animal，但Animal不可以看成Dog

	>>> def run_twice(animal):
		animal.run()
		animal.run()

		
	>>> run_twice(Animal())
	Animal is running
	Animal is running
	>>> run_twice(Dog())
	Dog is running...
	Dog is running...
	>>> run_twice(Cat())
	Cat is running.
	Cat is running.
	>>> class Tortoise(Animal):
		def run(self):
			print('Tortoise is running slowly.')

			
	>>> run_twice(Tortoise())	#tortoise = 陆龟
	Tortoise is running slowly.	#任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
	Tortoise is running slowly.

	由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
	对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法
	运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
		对扩展开放：允许新增Animal子类
		对修改封闭：不需要修改依赖Animal类型的, run_twice()等函数
	继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：

	                ┌───────────────┐
	                │    object     │
	                └───────────────┘
	                        │
	           ┌────────────┴────────────┐
	           │                         │
	           ▼                         ▼
	    ┌─────────────┐           ┌─────────────┐
	    │   Animal    │           │    Plant    │
	    └─────────────┘           └─────────────┘
	           │                         │
	     ┌─────┴──────┐            ┌─────┴──────┐
	     │            │            │            │
	     ▼            ▼            ▼            ▼
	┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
	│   Dog   │  │   Cat   │  │  Tree   │  │ Flower  │
	└─────────┘  └─────────┘  └─────────┘  └─────────┘


静态语言 vs 动态语言
	对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法
	对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
	>>> class Timer(object):
		def run(self):
			print('Start...')

	>>> timer = Timer()
	>>> timer.run()
	Start...
	Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
	你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

小结
	继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
	动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的


获取对象属性
	type() #判断对象类型

	基本类型都可以用, type()判断：
		>>> type(123)
		<class 'int'>
		>>> type('str')
		<class 'str'>
		>>> type(None)
		<type(None) 'NoneType'>

	如果一个变量指向函数或者类，也可以用, type()判断：
	>>> type(abs)
	<class 'builtin_function_or_method'>
	>>> type(a)
	<class '__main__.Animal'>

	type()函数它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
	>>> type(123)==type(321)
	True
	>>> type(123)==int
	True
	>>> type(123)==type('12')
	False
	>>> type('55')==str
	True

	判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
	>>> import types
	>>> def fn():
		pass

	>>> type(fn)==types.FunctionType
	True
	>>> type(abs)==types.FunctionType
	False
	>>> type(abs)==types.BuiltinFunctionType
	True
	>>> type(lambda x: x)==types.LambdaType
	True
	>>> type((x for x in range(10)))==types.GeneratorType
	True

	使用,isinstance()
	对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
	####isinstance()
		如果继承关系是:object -> Animal -> Dog -> Husky
		>>> a = Animal()
		>>> b = Dog()
		>>> c = Husky()
		Traceback (most recent call last):
		  File "<pyshell#339>", line 1, in <module>
		    c = Husky()
		NameError: name 'Husky' is not defined
		>>> c = Husky()
		>>> isinstance(c, Husky)
		True
		>>> class  Husky(Dog):
			def run(self):
				print('the dog is Husky')

				
		>>> isinstance(c, Dog)
		False
		>>> c = Husky()
		>>> isinstance(c, Dog)	#isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
		True	

		SO,Dog的b也是Animal类型
		>>> isinstance(b, Dog) and isinstance(b, Animal)
		True

		BUT
		>>> isinstance(b, Husky)
		False

		SO, 
		能用, type()判断的基本类型也可以用, isinstance()判断：
		>>> isinstance('a', str)
		True
		>>> isinstance(123, int)
		True
		>>> isinstance(b'a', bytes)
		True

		并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
		>>> isinstance([1, 2, 3], (list, tuple))
		True
		>>> isinstance([1, 2, 3], (tuple, list))
		True

		#####@@@@总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”


	使用, dir()
		如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
		比如，获得一个str对象的所有属性和方法：
			>>> dir('ABC')
			['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

		类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
	实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
	>>> len('ABC')
	3
	>>> 'ABC'.__len__()
	3

	我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
	>>> class Mymymy(object):
		def __len__(self):
			return 100

		
	>>> my = Mymymy()
	>>> len(my)
	100

	lower()返回小写的字符串：
	>>> 'SSSSSSS'.lower()
	'sssssss'

	仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
	>>> class MyObject(object):
		def __init__(self):
			self.x = 9
		def power(self):
			return self.x * self.x
		
	>>> obj = MyObject()

	可以测试该对象的属性：
	>>> hasattr(obj, 'x') # 有属性'x'吗？
	True
	>>> obj.x
	9
	>>> hasattr(obj, 'y') # 有属性'y'吗？
	False
	>>> setattr(obj, 'y', 19) # 设置一个属性'y'
	>>> hasattr(obj, 'y') # 有属性'y'吗？
	True
	>>> getattr(obj, 'y') # 获取属性'y'
	19
	>>> obj.y # 获取属性'y'
	19

	如果试图获取不存在的属性，会抛出AttributeError的错误
	>>> getattr(obj, 'q')
	Traceback (most recent call last):
	  File "<pyshell#411>", line 1, in <module>
	    getattr(obj, 'q')
	AttributeError: 'MyObject' object has no attribute 'q'

	可以传入一个default参数，如果属性不存在，就返回默认值：
	>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
	404

	也可以获得对象的方法：

	>>> hasattr(obj, 'power') # 有属性'power'吗？
	True
	>>> getattr(obj, 'power') # 获取属性'power'
	<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
	>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
	>>> fn # fn指向obj.power
	<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
	>>> fn() # 调用fn()与调用obj.power()是一样的
	81

# 小结
	通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：

	sum = obj.x + obj.y
	就不要写：

	sum = getattr(obj, 'x') + getattr(obj, 'y')
	一个正确的用法的例子如下：

	def readImage(fp):
	    if hasattr(fp, 'read'):
	        return readData(fp)
	    return None
	假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

	请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能

实例属性和类属性
	由于Python是动态语言，根据类创建的实例可以任意绑定属性

	给实例绑定属性的方法是通过实例变量，或者通过self变量：
	>>> class Student(object):
	    	name = 'Student'

	>>> s = Student() # 创建实例s
	>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
	Student
	>>> print(Student.name) # 打印类的name属性
	Student
	>>> s.name = 'Michael' # 给实例绑定name属性
	>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
	Michael
	>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
	Student
	>>> del s.name # 如果删除实例的name属性
	>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
	Student