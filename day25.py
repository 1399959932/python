#!usr/bin/python
序列化
	# 在程序运行的过程中，所有的变量都是在内存中
	d = dict(name='Ronin', age=21, score=88)
	# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'
	变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
	# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
	变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
	# Python提供了pickle模块来实现序列化
	import pickle
	>>> d = dict(name='Ronin', age=21, score=88)
	>>> pickle.dumps(d)	#pickle.dumps()方法把任意对象序列化成一个bytes
	b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x05\x00\x00\x00Roninq\x02X\x03\x00\x00\x00ageq\x03K\x15X\x05\x00\x00\x00scoreq\x04KXu.'
	
		pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
	或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
	# file-like Onject 即 #函数返回的这种有个, read()方法的对象

		当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
	也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
	>>> f = open('dump.txt', 'rb')
	>>> d = pickle.load(f)
	>>> f.close
	<built-in method close of _io.BufferedReader object at 0x02F3E1C8>
	>>> d
	{'name': 'Ronin', 'age': 21, 'score': 88}
	>>> f
	<_io.BufferedReader name='dump.txt'>

		Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
	因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

JSON
		我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式,比如XML，
	但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
	JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
	# JSON表示的对象就是标准的JavaScript语言的对象，
	JSON和Python内置的数据类型对应如下：
		JSON类型			Python类型
		{}				dict #字典,映射类型
		[]				list #列表
		"string"		str #字符串
		1234.56			int或float	#整数or浮点
		true/false		True/False #布尔
		null			None #空

	# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
	>>> import json
	>>> d = dict(name='Ronin', age=21, score=88)
	>>> json.dumps(d) #dumps()方法返回一个str，内容就是标准的JSON。
	'{"name": "Ronin", "age": 21, "score": 88}'

	dump()方法可以直接把JSON写入一个file-like Object
	要把JSON反序列化为Python对象, 
		loads()把JSON的字符串反序列化，
		load()把file-like Object中读取字符串并反序列化：

	>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
	>>> json.loads(json_str)
	{'age': 20, 'score': 88, 'name': 'Bob'}

	以下我的報錯了, 不排除是py版本的原因
	# >>> json_str = '{"age": 20, "score": 80, "name": "Ronin"}'
	# >>> json.loads(json_str)
	# Traceback (most recent call last):
	#   File "<pyshell#26>", line 1, in <module>
	#     json.loads(json_str)
	#   File "C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\lib\json\__init__.py", line 341, in loads
	#     if isinstance(s, str):
	# TypeError: isinstance() arg 2 must be a type or tuple of types

JSON进阶
	Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
	>>> import json
	>>> class Student(object):
		def __init__(self, name, age, score):
			self.name = name
			self.age = age
			self.score = score

			
	>>> s = Student('ROnin', 20 , 88)
	>>> print(s)
	<__main__.Student object at 0x02F6F4D0>
	>>> s
	<__main__.Student object at 0x02F6F4D0>
	>>> print(json.dumps(s)) #错误的原因是Student对象不是一个可序列化为JSON的对象
	Traceback (most recent call last):
	...
	TypeError: Object of type 'Student' is not JSON serializable

	dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了一大堆的可选参数：
	https://docs.python.org/3/library/json.html#json.dumps

	默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
		可选参数'default'就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
	我们写一个可以将student转换为json格式的函数, #利用参数'default'
	>>> def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

    >>> print(json.dumps(s, default=student2dict))	#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
	{"age": 20, "name": "Bob", "score": 88}

	# 把任意class的实例变为dict, 
	print(json.dumps(s, default=lambda obj: obj.__dict__))

	\lambda x: x * x  #关键字lambda表示匿名函数，冒号前面的x表示函数参数

	因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

		如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
	然后，我们传入的object_hook()函数负责把dict转换为Student实例：

	>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
	>>> print(json.loads(json_str, object_hook=dict2student))
	<__main__.Student object at 0x10cd3c190>
	报错了, 怀疑是版本问题
	# >>> json_str = '{"name": "Ronin", "age": 21, "score": 88}'
	# >>> print(json.loads(json_str, object_hook=dict2student))
	# Traceback (most recent call last):
	#   File "<pyshell#58>", line 1, in <module>
	#     print(json.loads(json_str, object_hook=dict2student))
	#   File "C:\Users\JK-chenxs\AppData\Local\Programs\Python\Python36-32\lib\json\__init__.py", line 341, in loads
	#     if isinstance(s, str):
	# TypeError: isinstance() arg 2 must be a type or tuple of types

小结
	Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
		json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
	既做到了接口简单易用，又做到了充分的扩展性和灵活性