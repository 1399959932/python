#!/usr/bin/python
print('今天是周一,因为周五辞职了,周六忙着投简历,周天搬家等快递,周一处理工资现在9点了准备学一个小时本来打算三个小时')

python标准异常总结
	AssertionError	断言语句 (assert) 失败
	IndexError	 	超出索引
	NameError		尝试访问一个不存在的变量
	OsError			操作系统产生的异常
	OverflowError	数字运算超过最大限制
	SyntaxError		语法错误
	TypeError		数据类型的操作错误
	ZeroDivisionError	出书为0
	ValueError		参数错误

异常检测
	try-exceot语句
	try:	
		检测范围
	except Exception[as reason]:
		出现异常(Exception)后的处理代码
	finally:
		无论如何都会被执行的代码

	例子:
		try:
	    f = open('我是文件.')
	    print(f.read())
		except OSError:/except (OSError,TypeError):
	    print('出错了')
		finally:
		  f.close()

	    ================ RESTART: C:\Users\JK-chenxs\Desktop\我是文件.py ================
		出错了

	例子:
		try:
	    f = open('我是文件.')
	    print(f.read())
	    f.close()
		except OSError as reason:
	    print('出错了:' + str(reason))

	    ================ RESTART: C:\Users\JK-chenxs\Desktop\我是文件.py ================
		出错了:[Errno 2] No such file or directory: '我是文件.

当'try'语句检测到错误时,会跳过下边找到'except'

raise
	>>> raise ZeroDivisionError
	Traceback (most recent call last):
	  File "<pyshell#4>", line 1, in <module>
	    raise ZeroDivisionError
	ZeroDivisionError

	>>> raise ZeroDivisionError('除数为零的异常')
	Traceback (most recent call last):
	  File "<pyshell#5>", line 1, in <module>
	    raise ZeroDivisionError('除数为零的异常')
	ZeroDivisionError: 除数为零的异常
# 小甲鱼该看34

列表生成式
	List Comprehensions是Python内置的非常简单却强大的可以用来创建list的生成式

	要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
	>>> list(range(1,11))
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
	>>> L = []
	>>> for x in range(1,11):
		L.append(x * x)

		
	>>> L
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

	= 

	>>> [x * x for x in range(1, 11)]
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

	#ps,突然察觉到了这个我应该是学过了,那也先不关了都开始了

	for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
	>>> [x * x for x in range(1, 11) if x % 2 == 0]
	[4, 16, 36, 64, 100]

	还可以使用两层循环，可以生成全排列：
	>>> [m + n for m in 'ABC' for n in 'XYZ']
	['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

	列出当前目录下的所有文件和目录名，可以通过一行代码实现：
	>>> import os
	>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
	['11.25.txt', '12.11左侧导航.txt', '3.8.docx', '8000.png', 'amz_4_baf', 'Composer-Setup.exe', 'cpts_435_sx', 'DedeCmsV5.6-UTF8-Final.tar.gz', 'desktop.ini', 'egpp_16_image-slider.zip', 'hasai.html', 'huawei.sql', 'IDLE (Python 3.6 32-bit).lnk', 'J', 'KK录像机.lnk', 'laravel.md', 'laravel.mom', 'laravelday2.md', 'learning.py', 'led', 'only.txt', 'php函数.jpg', 'project', 'py', 'QQBrowser_Setup_QB10beta3.exe', 'ss.html', 'Sublime Text Build 3126 x64', 'ThinkPay', 'UserController.php', 'web.php', 'work软', 'WPS H5.lnk', '分类标签.docx', '好压.lnk', '强哥视频', '我是文件.py', '搜狗高速浏览器.lnk', '文档3 - 副本.docx', '无标题.png', '最近的爱好.txt', '有道云协作.lnk', '有道云笔记.lnk', '有道云笔记网页剪报.url', '杂', '熊猫直播.lnk', '百度网盘.lnk', '省市区三级联动.sql', '简历模板', '计算机.lnk', '软', '逗游游戏盒.lnk', '金山文档修复.lnk', '阿里前台.url', '陈旭升(1).docx', '陈旭升.docx', '陈旭升docx.docx']

	for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
	>>> for k, v in d.items():
	print(k, '=', v)

	
	x = S
	y = D
	z = C

	列表生成式也可以使用两个变量来生成list：
	>>> [k + '=' + v for k, v in d.items()]
	['x=S', 'y=D', 'z=C']

	把一个list中所有的字符串变成小写：
	>>> S = ['Sss', 'Heool', 'world', 'im', 'Fine']
	>>> [s.lower() for s in S]
	['sss', 'heool', 'world', 'im', 'fine']

# 练习
	如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，
	所以列表生成式会报错：
	>>> S = [888, 'Heool', 'world', None, 'im', 'Fine']
	>>> [s.lower() for s in S]
	Traceback (most recent call last):
	  File "<pyshell#30>", line 1, in <module>
	    [s.lower() for s in S]
	  File "<pyshell#30>", line 1, in <listcomp>
	    [s.lower() for s in S]
	AttributeError: 'int' object has no attribute 'lower'
	使用内建的isinstance函数可以判断一个变量是不是字符串：
	>>> x = 'abc'
	>>> y = 123
	>>> isinstance(x, str)
	True
	>>> isinstance(y, str)
	False
	请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
	>>> L1 = ['Hello', 'World', 18, 'Apple', None]
	>>> L2 = [x.lower() for x in L1 if isinstance(x,str)]
	>>> L2
	['hello', 'world', 'apple']
	>>> L1
	['Hello', 'World', 18, 'Apple', None]
	>>> L2 = [s.lower() for s in L1 if isinstance(s,str)==True]
	>>> L2
	['hello', 'world', 'apple']

# 廖雪峰到高级特性的生成器