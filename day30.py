#!usr/bin/python
'datetime'
	datetime是Python处理日期和时间的标准库。

获取当前日期和时间
	>>> from datetime import datetime
	>>> now = datetime.now()	# 获取当前datetime
	>>> print(now)
	2018-05-09 19:59:00.028937
	>>> print(type(now))
	<class 'datetime.datetime'>
	注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
	如果仅导入import datetime，则必须引用全名datetime.datetime。
	datetime.now()返回当前日期和时间，其类型是datetime。

获取指定日期和时间
	# 要指定某个日期和时间，我们直接用参数构造一个datetime：
	>>> from datetime import datetime
	>>> dt = datetime(2018, 5, 13, 23, 59)
	>>> print(dt)
	2018-05-13 23:59:00
	>>> dt = datetime(2018, 5, 13, 23, 59, 59)
	>>> print(dt)
	2018-05-13 23:59:59

datetime转换为timestamp
	# 在计算机中，时间实际上是用数字表示的
	我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），
	当前时间就是相对于epoch time的秒数，称为timestamp。
	^SO,
	timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
	# 对应的北京时间
	timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00

		# timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
	# 这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。

	把一个datetime类型转换为timestamp只需要简单调用, timestamp()方法：
	>>> from datetime import datetime
	>>> dt = datetime(2018, 4, 9, 12, 50, 44)	## 用指定日期时间创建datetime
	>>> dt.timestamp()	# 把datetime转换为timestamp
	1523249444.0
	#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
	某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

timestamp转换为datetime
	timestamp #相当于1970 1 1 00:00:00(称为epoch time, 0) 对于相对于epoch time的秒数, 称为timestamp
	要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
	>>> from datetime import datetime
	>>> t = 1523249444.0
	>>> print(datetime.fromtimestamp(t))	#在timestamp和本地时间做转换。
	2018-04-09 12:50:44
	timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。

	>>> from datetime import datetime
	>>> t = 1523249444.0
	>>> print(datetime.fromtimestamp(t))	#本地时间
	2018-04-09 12:50:44
	>>> print(datetime.utcfromtimestamp(t))	#UTC时间
	2018-04-09 04:50:44

str转换为datetime
	# 很多时候，用户输入的日期和时间是字符串
	要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
	>>> from datetime import datetime
	>>> cday = datetime.strptime('2018-5-9 20:17:33', '%Y-%m-%d %H:%M:%S')
	#注意这里写法, 区分大小写
	>>> print(cday)
	2018-05-09 20:17:33	#转换后的datetime是没有时区信息的

	字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式

datetime转换为str
	# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，
	需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串
	>>> from datetime import datetime
	>>> now = datetime.now()
	>>> print(now.strftime('%a, %b, %d, %H:%M'))
	Wed, May, 09, 20:21

	'%a, %b, %d, %H:%M'	#星期 月份 日期 时:分

datetime加减
		对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
	加减可以直接用+和-运算符，不过需要导入timedelta这个类
	>>> from datetime import datetime, timedelta
	>>> now = datetime.now()
	>>> now
	datetime.datetime(2018, 5, 9, 20, 25, 16, 282094)
	>>> now + timedelta(hours=10)
	datetime.datetime(2018, 5, 10, 6, 25, 16, 282094)
	>>> now + timedelta(days=10)
	datetime.datetime(2018, 5, 19, 20, 25, 16, 282094)
	>>> now - timedelta(days=2, hours=6)
	datetime.datetime(2018, 5, 7, 14, 25, 16, 282094)

本地时间转为UTC时间
	本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
		一个datetime类型有一个时区属性tzinfo，但是默认为None，
	所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
	>>> from datetime import datetime, timedelta, timezone
	>>> utc_8 = timezone(timedelta(hours=8))	## 创建时区UTC+8:00
	>>> now = datetime.now()
	>>> now
	datetime.datetime(2018, 5, 9, 20, 30, 3, 467520)	
	>>> dt = now.replace(tzinfo=utc_8)	#强制设置为UTC+8:00
	>>> dt
	datetime.datetime(2018, 5, 9, 20, 30, 3, 467520, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))	
	#如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

时区转换
	通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
	# 拿到UTC时间，并强制设置时区为UTC+0:00:
	>>> utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)	
	>>> print(utc_dt)
	2018-05-09 12:33:57.221890+00:00

	# astimezone()将转换时区为北京时间:
	>>> bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
	>>> print(bj_dt)
	2018-05-09 20:33:57.221890+08:00

	# astimezone()将转换时区为东京时间:
	>>> tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
	>>> print(tokyo_dt)
	2018-05-09 21:33:57.221890+09:00
	
	## astimezone()将北京时间转换时区为东京时间:
	>>> tokyo2_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
	>>> print(tokyo2_dt)
	2018-05-09 21:33:57.221890+09:00

	# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
	利用带时区的datetime，通过astimezone()方法，可以转换到任意时区
	不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

小结
	datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

	如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。


^collections
	collections是Python内建的一个集合模块，提供了许多有用的集合类。

namedtuple
	tuple可以表示不变集合 #元祖()
	# 用法	表示一个坐标
	>>> from collections import namedtuple
	>>> Point = namedtuple('Point', ['x', 'y'])
	>>> p = Point(1, 2)
	>>> p.x
	1
	>>> p.y
	2
	namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
	namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
	namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

	用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用
	# 可以验证创建的Point对象是tuple的一种子类：
	>>> isinstance(p, Point)
	True
	>>> isinstance(p, tuple)
	True

	#用坐标和半径表示一个圆
	# namedtuple('名称', [属性list]):
	Circle = namedtuple('Circle', ['x', 'y', 'r'])

deque
	使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

	deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
	>>> from collections import deque
	>>> q = deque(['a', 'b', 'c'])
	>>> q.append('x')	#尾部添加
	>>> q.appendleft('y')	#头部添加元素
	>>> q
	deque(['y', 'a', 'b', 'c', 'x'])

	deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

defaultdict
	使用dict时，如果引用的Key不存在，就会抛出KeyError。
	>>> c = {'a':1, 'b':2, 'c':'chen'}
	>>> c
	{'a': 1, 'b': 2, 'c': 'chen'}
	>>> c['a']
	1
	>>> c['d']
	Traceback (most recent call last):
	  File "<pyshell#83>", line 1, in <module>
	    c['d']
	KeyError: 'd'

	如果希望key不存在时，返回一个默认值，就可以用defaultdict：
	>>> from collections import defaultdict
	>>> dd = defaultdict(lambda: 'N/A')
	>>> dd['key1'] = 'abc'	## key1存在
	'abc'
	>>> dd['key2']	#key2不存在，返回默认值
	'N/A'
	# 默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
	除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

OrdereddDict
	使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
	如果要保持Key的顺序，可以用OrderedDict：
	>>> from collections import OrderedDict
	>>> d = dict([('a', 'apple'), ('b', 'boy'), ('c', 'china')])
	>>> d
	{'a': 'apple', 'b': 'boy', 'c': 'china'}
	>>> od = OrderedDict([('a', 'apple'), ('b', 'boy'), ('c', 'china')])
	>>> d
	{'a': 'apple', 'b': 'boy', 'c': 'china'}
	>>> d
	{'a': 'apple', 'b': 'boy', 'c': 'china'}
	>>> d
	{'a': 'apple', 'b': 'boy', 'c': 'china'}

	##我试了很多次都是有序的, 廖的网站写的# dict的Key是无序的不知道是不是版本问题
	>>> od # # OrderedDict的Key是有序的
	OrderedDict([('a', 'apple'), ('b', 'boy'), ('c', 'china')])

	OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
	#即
	from collections import OrderedDict

	class LastUpdatedOrderedDict(OrderedDict):

	    def __init__(self, capacity):
	        super(LastUpdatedOrderedDict, self).__init__()
	        self._capacity = capacity

	    def __setitem__(self, key, value):
	        containsKey = 1 if key in self else 0
	        if len(self) - containsKey >= self._capacity:
	            last = self.popitem(last=False)
	            print('remove:', last)
	        if containsKey:
	            del self[key]
	            print('set:', (key, value))
	        else:
	            print('add:', (key, value))
	        OrderedDict.__setitem__(self, key, value)

Counter
	Counter是一个简单的计数器，例如，统计字符出现的个数：
	>>> from collections import Counter
	>>> c = Counter()
	>>> for ch in 'chen ronin is big good boy':
		c[ch] = c[ch] + 1

		
	>>> c
	Counter({' ': 5, 'o': 4, 'n': 3, 'i': 3, 'b': 2, 'g': 2, 'c': 1, 'h': 1, 'e': 1, 'r': 1, 's': 1, 'd': 1, 'y': 1})
