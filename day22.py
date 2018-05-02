#!usr/bin/python
调试
	通过print()
	如下
断言	
	凡是用, print()来辅助查看的地方，都可以用断言（assert）来替代
	>>> def foo(s):
		n = int(s)
		print('>>> n = %d' % n)#等于下
		assert n != 0, 'n is zero!'
		#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
		return 10 / n

	>>> def main():
		foo('0')

		
	>>> main()
	>>> n = 0
	Traceback (most recent call last):
	  File "<pyshell#8>", line 1, in <module>
	    main()
	  File "<pyshell#7>", line 2, in main
	    foo('0')
	  File "<pyshell#4>", line 4, in foo
	    return 10 / n
	ZeroDivisionError: division by zero

	#assert 断言失败assert语句本身就会抛出AssertionError：
	assert n != 0, 'n is zero!'
	AssertionError: n is zero!

logging
	把print()替换为logging是第三种, 和assert比，logging不会抛出错误，而且可以输出到文件：
	import logging
	logging.basicConfig(level=logging.INFO)#不加这行只报错没有提示

	s = '0'
	n = int(s)
	logging.info('n = %d' % n)
	print(10 / n)
	# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息
	# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件

pdb	
	# 第四种
	# 要检查的py文件
	s = '0'
	n = int(s)
	print(10 / n)

	# 命令行执行
	$ python -m pdd day22.py
	> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
	-> s = '0'
	#进入pdb模式后, 可以用p var, 查看变量
	p n
	q	#退出程序
	#but
		# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊
pdb.set_trace()
	这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
	import pdb

	s = '0'
	n = int(s)
	pdb.set_trace() # 运行到这里会自动暂停
	print(10 / n)
	命令c继续运行

IDE
	如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：

	Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。

	PyCharm：http://www.jetbrains.com/pycharm/

	另外，Eclipse加上pydev插件也可以调试Python程序。

小结
	写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。

	虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。


单元测试, (没咋看)
	mydict.py代码如下：

	class Dict(dict):

	    def __init__(self, **kw):
	        super().__init__(**kw)

	    def __getattr__(self, key):
	        try:
	            return self[key]
	        except KeyError:
	            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	    def __setattr__(self, key, value):
	        self[key] = value
	为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

	import unittest

	from mydict import Dict

	class TestDict(unittest.TestCase):

	    def test_init(self):
	        d = Dict(a=1, b='test')
	        self.assertEqual(d.a, 1)
	        self.assertEqual(d.b, 'test')
	        self.assertTrue(isinstance(d, dict))

	    def test_key(self):
	        d = Dict()
	        d['key'] = 'value'
	        self.assertEqual(d.key, 'value')

	    def test_attr(self):
	        d = Dict()
	        d.key = 'value'
	        self.assertTrue('key' in d)
	        self.assertEqual(d['key'], 'value')

	    def test_keyerror(self):
	        d = Dict()
	        with self.assertRaises(KeyError):
	            value = d['empty']

	    def test_attrerror(self):
	        d = Dict()
	        with self.assertRaises(AttributeError):
	            value = d.empty
	编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

	以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

	对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

	self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
	另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：

	with self.assertRaises(KeyError):
	    value = d['empty']
	而通过d.empty访问不存在的key时，我们期待抛出AttributeError：

	with self.assertRaises(AttributeError):
	    value = d.empty

运行单元测试
	一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：

	if __name__ == '__main__':
	    unittest.main()

setUp与tearDown
	可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

	setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

	class TestDict(unittest.TestCase):

	    def setUp(self):
	        print('setUp...')

	    def tearDown(self):
	        print('tearDown...')
	可以再次运行测试看看每个测试方法调用前后是否会打印出setUp...和tearDown...。