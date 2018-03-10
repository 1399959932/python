#!/usr/bin/python
# print('今天周五,需要赶进度了')
# 今天目标三百行然后去看php

dict{},字典
fromkeys()
	dict.fromkeys(S[,v]) ,v不提供的话,默认为None,例:
	>>> dict1 = {}
	>>> dict1.fromkeys((1, 2, 3))
	{1: None, 2: None, 3: None}
	>>> dict1.formkeys((1, 2, 3, 'Number'))
	>>> dict1.fromkeys((1, 2, 3), 'Number')
	{1: 'Number', 2: 'Number', 3: 'Number'}
	>>> dict1.fromkeys((1, 2, 3), ('one', 'two', 'three'))
	{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}

	>>> dict1 = dict1.fromkeys(range(32), 'k')

	>>> for eachValue in dict1.Value():
	print(eachValue)

	>>> for eachValue in dict1.values():
	print(eachValue)

	>>> for eachItem in dict1.items(): #打印项
	print(eachItem)

	print(dict1[31])
	>>> print(dict1.get(32))
	None
	>>> print(dict1.get(32, '木有'))
	木有
	>>> print(dict1.get(31, '木有'))
	k

	清除字典,clear()
	>>> dict1.clear()

	copy() ,浅拷贝,只是对对象表层的拷贝
	id(),返回地址

	>>> a = {1:'one', 2:'two', 3:'three'}
	>>> b = a
	>>> c = b.copy()
	>>> b
	{1: 'one', 2: 'two', 3: 'three'}
	>>> c
	{1: 'one', 2: 'two', 3: 'three'}
	>>> id(a)
	51869856
	>>> id(b)
	51869856
	>>> id(c) #浅拷贝
	51870336 
	>>> 

	赋值的话>>>a = b, 单修改a, b也会变,但是,copy()方法不会
	pop('i'), 给定键弹出值
	popitem(), 给定键弹出项 

	>>> b.pop()
	Traceback (most recent call last):
	  File "<pyshell#38>", line 1, in <module>
	    b.pop()
	TypeError: pop expected at least 1 arguments, got 0
	>>> b.popitem()
	(3, 'three')
	>>> b
	{1: 'one'}
	>>> c
	{1: 'one', 2: 'two', 3: 'three'}
	>>> a
	{1: 'one'}
	>>> c
	{1: 'one', 2: 'two', 3: 'three'}
	>>> b
	{1: 'one'}
	>>> 

	setdefault(), 随机向字典添加项,因为字典没有顺序
	>>> c.setdefault('white')
	>>> c
	{1: 'one', 2: 'two', 3: 'three', 'white': None}

	update(), 根据k修改自己的值
	>>> b = {'小白':'狗'}
	>>> c.update(b)
	>>> c
	{1: 'one', 2: 'two', 3: 'three', 'white': None, '小白': '狗'}

set,集合
	用{1,2,3,4,5}扩起一对一堆数字,而且数字没有体现映射关系事,就是集合
	>>> num = {}
	>>> type(num)
	<class 'dict'>
	>>> num1 = {1, 2, 3, 4}
	>>> type(num1)
	<class 'set'>

	# 创建集合
	>>> num1 = {11,2,1,211,2,1,3,4,5,5,3} #用{}圈起int
	>>> num1
	{1, 2, 3, 4, 5, 11, 211} #重复的会被剔除
	>>> num1[2]
	Traceback (most recent call last):
	  File "<pyshell#59>", line 1, in <module>
	    num1[2]
	TypeError: 'set' object does not support indexing

	>>> num3 = set([1, 2, 3, 4, 5, 5, 4]) #通过set([i, i])创建
	>>> num3
	{1, 2, 3, 4, 5}

	去除list[0, 1, 2, 3, 4, 0, 2, 4, 5]多余的元素
	# page1:
	>>> list = [0, 1, 2, 3, 4, 0, 2, 4, 5]
	>>> temp = []
	>>> for each in list:
		if each not in temp:
			temp.append(each)

			
	>>> temp
	[0, 1, 2, 3, 4, 5]

	# page2
	>>> num1 = list(set(list)) #set()没有顺序,顺序会错
	Traceback (most recent call last):
	  File "<pyshell#73>", line 1, in <module>
	    num1 = list(set(list))
	TypeError: 'list' object is not callable #类型错误：“list”对象不可调用
	会报错,我觉得是不是版本问题

frozen #不可变集合 frozen:冰冻的,冻结的
	>>> num2 = frozenset(num1)
	>>> num2
	frozenset({0, 1, 2, 3, 4, 5})

	>>> num1
	{0, 1, 2, 3, 4, 5}
	>>> num1.add(6)
	>>> num1
	{0, 1, 2, 3, 4, 5, 6}
	>>> num2.add(6) # 不可变集合,所以无法添加
	Traceback (most recent call last):
	  File "<pyshell#90>", line 1, in <module>
	    num2.add(6)
	AttributeError: 'frozenset' object has no attribute 'add'

open() #打开文件
	>>> f = open('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\Day\\day11p.txt')
		# '\\' = '\' ,使用'\',需要转译'\\',或者使用'/'
	>>> f
	<_io.TextIOWrapper name='C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\Day\\day11p.txt' mode='r' encoding='cp936'>
	>>> f.read()
	'今天3.9\n昨天晚上不给看新闻说气温回暖'

	f.close()	关闭文件
	f.read(size=-1)	从文件读取size个字符
		>>> f = open('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\Day\\day11p.txt')
		>>> f.read(5)
		'今天3.9'
	f.tell()	返回当前在文件中的位置
		>>> f.tell()
		7
	f.readline()	以写入模式打开,如果文件存在,则在末未追加写入
	f.seek(offset, from)	在文件中移动文件指针,从from(0代表文件起始位置,1代表当前位置,2代表文件末尾)
	偏移offset个字节
		>>> f.seek(8, 0)
		8
		>>> f.readline()
		'昨天晚上不给看新闻说气温回暖'
	f.write(str)	降字符串写入文件
	>>> f = open('C:/Users/JK-chenxs/AppData/Local/Programs/Python/Python36-32/Day/day11p.txt', 'w') #'w',注意这个w,代表权限
	>>> f.write('这几天怎么这么困')
	8
	>>> f.close()

	>>> for each_line in f:
		print(each_line)

	
	今天3.9 昨天晚上不给看新闻说气温回暖


模块, 是一个包含所以你定义的函数和变量的文件,后缀为py
模块可以被别的程序引入,以使用该模块中的函数等功能
	>>> secret = random_randint(1, 10)
	Traceback (most recent call last):
	  File "<pyshell#1>", line 1, in <module>
	    secret = random_randint(1, 10)
	NameError: name 'random_randint' is not defined
	>>> import random
	>>> secret = random.randint(1, 10)
	>>> secret

OS:操作系统
	getcwd() 	#返回当前的工作目录
	>>> os.getcwd()
	Traceback (most recent call last):
	  File "<pyshell#10>", line 1, in <module>
	    os.getcwd()
	AttributeError: module 'os' has no attribute 'geicwd'
	>>> import os
	>>> os.getcwd()
	'C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32'

	chdir(path)	#改变工作目录

	listdir(path='.')	#列举指定目录中的文件名('.'表示当前目录,'..'表示上记忆目录	)
	>>> os.listdir('E:\\')
	['$RECYCLE.BIN', '.git', 'led', 'Netease', 'python', 'System Volume Information', 'wamp64', '英雄联盟']	
	
	mkdir(path)	#创建单层目录,如该目录已存在抛出异常
	单层,即有父级才能创建子级
	>>> os.mkdir('E:\\A')
	>>> os.mkdir('E:\\A\\b')

	makedirs(path) #创建多层目录,如该目录已存在抛出异常
	>>> os.makedirs('E:\\b\\c')

	rmdir(path)	#删除单层目录
	>>> os.rmdir('E:\\A\\b')
	>>> os.rmdir('E:\\A')

	removedirs(path)	#递归删除
	>>> os.removedirs('E:\\b\\c')

	rename(old, new)	#将文件old名字替换为new

	system('cmd')	#运行系统的shell命令,cms为计算机
	>>> os.system('cms')
	1
	>>> os.system('cmd')
	-1073741510

	os.curdir	#指带当前目录('.')

	os.pardir	#指带上一级目录('.')

	os.sep	#输出操作系统特定的路径分隔符 win'\\',linux'/'

	os.linesep	#当前平台使用的行终止符win'\r\n',linux'\n'
	os.name 	#指带当前使用的操作系统

os.path
	basename(path)	#去掉文件目录,返回文件名
	>>> os.path.basename('E:\\led')
	'led'

	dirname(path)	#qu掉文件名,返回目录
	>>> os.path.dirname('E:\\led')
	'E:\\

	join(path1[,path2[, ...]])	#将path1,path2个副本组合成一个路径名

	split(path)	#分割文件名与路径
	>>> os.path.split('E:\\led')
	('E:\\', 'led')	#一定会返回这种形式,不管'led'是文件还是路径

	splitext(path)	#分离文件名和扩展名
	>>> os.path.splitext('E:\\led')
	('E:\\led', '')

	getsize(file)	#返回文件大小,单位为b

	getatime(file)	#返回指定文件最近的访问时间

	getctime(file)	#返回指定文件最新的穿件时间
	
	getmtime(file)	#返回指定文件最新的修改时间

	exists(path)	#判断指定路径(目录或文件)是否存在

	isabs(path)		#判断指定路径是否为绝对路径

	isdir(path)		#判断指定路径是否存在且是一个目录

	isfile(path)	#判断指定路径是否存在且是一个文件

	islink(path)		#判断指定路径是否存在且是一个符号链接(快捷方式)

	isdir(path)		#判断指定路径是否存在且是一个目录

	ismount(path)		#判断指定路径是否存在且是一个挂载点(磁盘)

	samefile(path1, path2)	#判断1,2两个路径是否指定同一个文件

# 存放:pickling
# 读取:unpickling
模块,pickle永久储存

	>>> import pickle
	>>> my_list = [123, 3.14, '陈老爷' , ['pic', 1]]
	>>> pickle_file = open('my_list.pkl', 'wb') #'wb',二进制的写入形式
	>>> pickle.dump(my_list, pickle_file)		#dump()放进
	>>> pickle_file.close()
	>>> pick_file = open('my_list.pkl', 'rb')	#'rb',二进制的读取形式
	>>> my_list2 = pickle.load(pick_file)
	>>> print(my_list2)
	[123, 3.14, '陈老爷', ['pic', 1]]

# 廖雪峰
	# 打印1到100的奇数
	l = []
	n = 1
	while n <= 99:
		l.append(n)
		n = n + 2

	print(list(range(1,100,2)))

# 切片
	>>> L = ['s', 'q', 't', 'j', 'q', 'o']
	>>> L[:3]	#提取前三个元素,直到索引3为止，但不包括索引3
	['s', 'q', 't']
	# 倒数第一个元素的索引是-1
	>>> L[:10:2]	#前10个数，每两个取一个：
	['s', 't', 'q']
	>>> L[::5]	#所有书,每5个娶一个
	['s', 'o']
	>>>L[:]		#甚至什么都不写，只写[:]就可以原样复制一个list：
	['s', 'q', 't', 'j', 'q', 'o']

	tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

	>>> (0, 1, 2, 3, 4, 5)[:3]
	(0, 1, 2)	#还是tuple

	字符串'xxx'也可以看成是一种list，每个元素就是一个字符
	>>> 'ABCDEFG'[:3]
	'ABC'	#返回值为str
	>>> 'ABCDEFG'[::2]
	'ACEG'

	练习	# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
	
	def trim(s):
	    if s == '':
	        return s
	    elif s[0] == ' ':
	        return trim(s[1:])
	    elif s[-1] == ' ':
	        return trim(s[:-1])
	    return s