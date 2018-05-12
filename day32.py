#/usr/bin/python
hashlib
摘要算法简介
	Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
	# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
	摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

	摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
	#我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
	import hashlib

	>>> md5 = hashlib.md5()
	>>> md5.update('my name is chen ronin.'.encode('utf-8'))
	>>> print(md5.hexdigest())
	6fe3bec2b24af97667d0ed055e16624a
	# 如果数据量很大，可以分块多次调用update()，

	>>> md5.update('my name is chen ronin.'.encode('utf-8'))
	>>> md5.update('im is good boy hahah !'.encode('utf-8'))
	>>> print(md5.hexdigest())
	1b37e3827bead49b48554488bfe42abb	#即使改动一个字母也会完全变化
	# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

	# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
	>>> import hashlib
	>>> 
	>>> sha1 = hashlib.sha1()
	>>> sha1.update('this is sha1 in'.encode('utf-8'))
	>>> sha1.update('today is friday'.encode('utf-8'))
	>>> print(sha1.hexdigest())
	1f16d64290c281dc105c1239782592806b67b663	#SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示

	# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞

摘要算法应用
	
hmac
	通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希
	# 用保存在数据库中的password_md5对比计算md5(password)的结果，如果一致，用户输入的口令就是正确的
	
		为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，
	需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。	

	如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)
	# 实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中

	#例子, 首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下
	>>> import hmac
	>>> message = b'ronin'
	
	>>> key = b'chen'
	>>> s = hmac.new(key, message, digestmod='MD5')
	# 如果消息很长，可以多次调用h.update(msg)
	>>> s.hexdigest()
	'8f39aa9f54d8ba4a1920c4d84d4e5573

itertools
	Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
	>>> import itertools
	>>> natuals = itertools.count(1)	#count()会创建一个无限的迭代器
	>>> for n in natuals:
		print(n)

		count()会创建一个无限的迭代器，
	所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出

	# cycle()会把传入的一个序列无限重复下去：
	>>> import itertools
	>>> cs = itertools.cycle('ROnin')	#cycle()会把传入的一个序列无限重复下去：
	>>> for c in cs:
		print(c)

	# 同样停不下来

		repeat()负责把一个元素无限重复下去，
	不过如果提供第二个参数就可以限定重复次数：
	>>> import itertools
	>>> ns = itertools.repeat('SS', 9)
	>>> for n in ns:
		print(ns)

		
	repeat('SS', 8)
	repeat('SS', 7)
	repeat('SS', 6)
	repeat('SS', 5)
	repeat('SS', 4)
	repeat('SS', 3)
	repeat('SS', 2)
	repeat('SS', 1)
	repeat('SS', 0)

		无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
	它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

		# 无限序列虽然可以无限迭代下去，但是通常我们会通过
	takewhile()等函数根据条件判断来截取出一个有限的序列：
	>>> import itertools
	>>> natuals = itertools.count(1)
	>>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
	>>> list(ns)
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

chain()
	chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
	>>> import itertools
	>>> for c in itertools.chain('ABCD', 'EFG'):
		print(c)

		
	A
	B
	C
	D
	E
	F
	G

groupby()
	groupby()把迭代器中相邻的重复元素挑出来放在一起：
	>>> for key, group in itertools.groupby('aazzxxssddcc', lambda c: c.upper()):
		print(key, list(group))

		
	A ['a', 'a']
	Z ['z', 'z']
	X ['x', 'x']
	S ['s', 's']
	D ['d', 'd']
	C ['c', 'c']

	只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
	>>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	...     print(key, list(group))
	...
	A ['A', 'a', 'a']
	B ['B', 'B', 'b']
	C ['c', 'C']
	A ['A', 'A', 'a']

小结
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。


