#!/usr/bin/python
print()

模块Module
	在Python中，一个.py文件就称之为一个模块（Module）
	使用模块还可以避免函数名和变量名冲突。但是也要注意，尽量不要与内置函数名字冲突

	举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
	现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放
		mycompany
		├─ __init__.py
		├─ abc.py
		└─ xyz.py
		引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz
	!!!请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，
	!!!Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany

	类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：
		mycompany
		 ├─ web
		 │  ├─ __init__.py
		 │  ├─ utils.py
		 │  └─ www.py
		 ├─ __init__.py
		 ├─ abc.py
		 └─ xyz.py
	 	文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils

 	!$! 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块
	mycompany.web也是一个模块，请指出该模块对应的.py文件

# 总结
	模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
	创建自己的模块时，要注意：

	模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
	模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块

# 使用模块
	我们以内建的sys模块为例，编写一个hello的模块：
	sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
		运行python3 hello.py获得的sys.argv就是['hello.py']；
		运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]
	
		#!/usr/bin/env python3
	# -*- coding: utf-8 -*-

	' a test module '	#是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

	__author__ = 'Ronin Chen'	#使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

	import sys

	def test():
	    args = sys.argv
	    if len(args)==1:
	        print('Hello, world!')
	    elif len(args)==2:
	        print('Hello, %s!' % args[1])
	    else:
	        print('Too many arguments!')

	if __name__=='__main__':
	    test()

	    当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，
	    if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

	我们可以用命令行运行hello.py看看效果：

	$ python hello.py #运行python hello.py获得的sys.argv就是['hello.py']；
	Hello, world!
	$ python hello.py Michael #运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。
	Hello, Michael!
	如果启动Python交互环境，再导入hello模块：

	$ python3
	Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
	[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import hello
	>>>
	导入时，没有打印Hello, word!，因为没有执行test()函数。

	调用hello.test()时，才能打印出Hello, word!：

	>>> hello.test()
	Hello, world!

# 作用域:
	正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI
	
	似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
	hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名

	类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc
	之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量
	private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

	>>> def _private_1(name):
	return 'Hello, %s' % name

	>>> def _private_2(name):
		return 'Hi, %s' % name

	>>> def greeting(name):
		if len(name) > 3:
			return _private_1(name)
		else:
			return _private_2(name)

		>>> _private_1('chen')
		'Hello, chen'

		>>> greeting(chen)
		Traceback (most recent call last):
		  File "<pyshell#49>", line 1, in <module>
		    greeting(chen)
		NameError: name 'chen' is not defined

		>>> greeting('chen')
		'Hello, chen'
		>>> greeting('s')
		'Hi, s'
	SO,	外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public

# 安装第三方模块
	在Python中，安装第三方模块，是通过包管理工具pip完成的

	我们要安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3

Anaconda
	，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用

模块搜索路径
	当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：

	>>> import mymodule
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ImportError: No module named mymodule
	默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

	>>> import sys
	>>> sys.path
	['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', ..., '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
	如果我们要添加自己的搜索目录，有两种方法：

	一是直接修改sys.path，添加要搜索的目录：

	>>> import sys
	>>> sys.path.append('/Users/michael/my_py_scripts')
	这种方法是在运行时修改，运行结束后失效。

	第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。面向函数编程

面向对象编程
	面向对象编程——Object Oriented Programming	 简称OOP，是一种程序设计思想
	OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

	>>> class Student(object):
		def __init__(self, name, score):
			self.name = name
			self.score = score
		def print_score(self):
			print('%s: %s' % (self.name, self.score))

			
	>>> chen = Student('Boy chen', 99)
	>>> chen.print
	Traceback (most recent call last):
	  File "<pyshell#70>", line 1, in <module>
	    chen.print
	AttributeError: 'Student' object has no attribute 'print'
	>>> chen.print_score()
	Boy chen: 99

	面向对象的设计思想是抽象出Class，根据Class创建Instanc
	面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法

小结
	数据封装、继承和多态是面向对象的三大特点