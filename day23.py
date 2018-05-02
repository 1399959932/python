#!usr/bin/python
文档测试
	>>> import re
	>>> m = re.search('(?<=abc)def', 'abcdef')
	>>> m.group(0)
	'def'
	# “文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
	
	def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

IO编程
	IO Input/Output, 也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。
	往外发数据，叫Output，#把数据写到磁盘文件里，就只是一个Output操作
	从外面接收数据，#从磁盘读取文件到内存，就只有Input操作，
	
	stream	流
	Input Stream就是数据从外面（磁盘、网络）流进内存
	Output Stream就是数据从内存流到外面去

	同步IO cpu等程序运行结束再往下执行, 
	异步IO cpu去做别的, 告诉程序执行这个

文件读写
	>>> f = open('/Users/michael/test.txt', 'r')#('文件名', '标识符')
	!!!打开之后必须关闭, close()
	>>> f.close()

	由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
	try:
	    f = open('/path/to/file', 'r')
	    print(f.read())
	finally:
	    if f:
	        f.close()
	===
	with 语句

	with open('/path/to/file', 'r') as f:
    	print(f.read())

    read(size)	#反复调用
    readline()可以每次读取一行内容
    readlines()一次读取所有内容并按行返回list
	    for line in f.readlines():
	    print(line.strip()) # 把末尾的'\n'删掉

file-like Object
	像 open(), 函数返回的这种有个, read()方法的对象，在Python中统称为file-like Object。
	除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
	StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

二进制文件
	要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

	>>> f = open('/Users/michael/test.jpg', 'rb')#读取二进制
	>>> f.read()
	b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

字符编码
	要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

	>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
	>>> f.read()
	'测试'

	open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
	>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

写文件
	>>> f = open('/Users/michael/test.txt', 'w') #'w'或者'wb'
	>>> f.write('Hello, world!')
	>>> f.close()	####不写程序 write()是在内存的, 不会保证全部写入

	so
	with open('/Users/michael/test.txt', 'w') as f:
    	f.write('Hello, world!')
    以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
    https://docs.python.org/3/library/functions.html#open