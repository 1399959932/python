#!usr/bin/python
StringIO	#在内存中读写str
	# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
	>>> from io import StringIO
	>>> f = StringIO()
	>>> f.write('hello')
	5
	>>> f.write('h')
	1
	>>> f.write('')
	0
	>>> f.write(' ')
	1
	>>> f.getvalue()	#getvalue()用于 获得写入后的str
	'helloh '
	>>> print(f.getvalue())
	helloh 

	# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
	>>> from io import StringIO
	>>> f = StringIO('Hello!\nhi!\nGoodbyebye!')
	>>> while True:
		s = f.readline()
		if s== '':
			break
		print(s.strip())

		
	Hello!
	hi!
	Goodbyebye!

BytesIO
	StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
	>>> from io import BytesIO
	>>> f = BytesIO()
	>>> f.write('中文'.encode('utf-8'))	#写入的不是str，而是经过UTF-8编码的bytes
	6
	>>> print(f.getvalue())
	b'\xe4\xb8\xad\xe6\x96\x87'

	# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取
	>>> from io import BytesIO
	>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
	>>> f.read()
	b'\xe4\xb8\xad\xe6\x96\x87'

StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口

操作文件和目录
	Python内置的os模块也可以直接调用操作系统提供的接口函数
	>>> import os
	>>> os.name # 操作系统类型
	'nt'	#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统

	>>> os.uname()	#详细的系统信息, window下不提供
	posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')
	# Traceback (most recent call last):
	#   File "<pyshell#31>", line 1, in <module>
	#     os.uname()
	# AttributeError: module 'os' has no attribute 'unam

环境变量
	在操作系统中定义的环境变量，全部保存在os.environ这个变量中
	>>> os.environ
	environ({'', ''})
	>>> os.environ.get('PATH')	#获取某个环境变量的值，可以调用os.environ.get('key')
	>>> os.environ.get('x', 'default')
	'default'

操作文件和目录
	操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块
	>>> os.path.abspath('.')	# 查看当前目录的绝对路径:
	'C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32'
	# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
	>>> os.path.join('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32', 'testdir')
	'C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir'
	# 然后创建一个目录:
	>>> os.mkdir('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir')
	# 删掉一个目录
	>>> os.rmdir('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir')

	把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
	# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
	part-1/part-2
	# 而Windows下会返回这样的字符串：
	part-1\part-2

	合成路径 os.path.join()
	拆分路径 os.path.split()
	###这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

	拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
	>>> os.path.split('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir\\file.txt')
	('C:\\Users\\JK-chenxs\\AppData\\Local\\Programs\\Python\\Python36-32\\testdir', 'file.txt')

	获取文件扩展名 os.path.splitext()
	>>> os.path.splitext('/path/to/file.txt')
	('/path/to/file', '.txt')

	# 对文件重命名:
	>>> os.rename('test.txt', 'test.py')
	# 删掉文件:
	>>> os.remove('test.py')

	shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
	#列出所有的.py文件
	>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
	[]

	#列出当前目录下的所有目录
	>>> [x for x in os.listdir('.') if os.path.isdir(x)]
	['.git', 'A', 'Day', 'DLLs', 'Doc', 'include', 'Lib', 'libs', 'Scripts', 'tcl', 'Tools']

Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。