# C:/Users/JK-chenxs/AppData/Local/Programs/Python
# python内置数据类型:
# 列表:list是一种有序的集合,可以随时添加删除其中的元素 优点:方便操作
	# classmates = ['Micheal','Bob','JK-chenxs']
	# classmates
	# len(classmates)
	# php的数组array 相似与 python的列表list
	# len()返回容器中的项数 	我理解为长度或者是个数

	# classmates[0]
	# -1可以取最后一个元素,以此类推

	# list操作方法 ,以下 'var' = '变量'' ,python叫元素
	# 增
	# 	list.append('var1') 
	# 		append插入元素1到list末尾
	#	list.extend(['var1', 'var2'])
	#		extend插入若干元素,以list列表(数组)形式添加
	# 	list.insert(1, 'var1')
	# 		insert插入元素1到索引1位置
	# 删
	# 	list.pop(i)
	# 		pop删除list末尾的元素
	# 		删除指定位置添加索引i
	# 改
	# 	list[1] = 'var1'
	# 	替换的话直接给list索引重新赋值即可

	# list中元素的数据类型也可以不同
	# list就是数组,内部元素也可以是list(二维数组)
	# 提取二维list中的元素可以用 list[i], list[i][i] 内部集合[索引], 外部list[i][i]

# 元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改 优点:安全
	# 格式
		# classmates = ('Micheal','Bob','JK-chenxs')

	# 查询 
		# classmates[0]

	# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
		# 例: c = ('chen',)

	# 当tuple内嵌入list时,元素不变(不能被赋值,也不能更换索引),单list内的元素可以改变,即
		# s = ('a', 'b', ['c', 'd'])
		# s[2][1] = 'c'
		# s[2][0] = 'd'
		# a,b是不能变的[]内可以随便操作(增删改)
			# .append(), .append(i, '')
			# .pop(), .pop(i)
			# 改: s[i][i] = ''

# 条件判断,每句判断关键词后边都要加,冒号':'
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
	# 单if
	# age = 20
	# if age >= 18:
	# 	print('your age is', age)
	# 	print('adult')

	# if else
	# age = 22
	# if age >= 18:
	# 	print('your age is', age)
	# 	print('adult')
	# else:
	# 	print('your age is', age)
	# 	print('teenager')

	# elif是 else if 的缩写		
	# age = 16
	# if age >= 18:
	# 	print('adult')
	# elif age >= 6:
	# 	print('teenager')
	# else:
	# 	print('kid')

	# 即
	# if <条件判断1>:
	# 	<执行1>
	# elif <条件判断2>:
	# 	<执行2>
	# elif <条件判断3>:
	# 	<执行3>
	# else:
	# 	<执行4>

	# if判断条件还简写
	# if x:
 	# 	print('True')
 	# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else


# input()
	# input()返回的数据类型是str,所以不能直接和整数比较需要使用int()转化
	# s = input('birth: ')
	# birth = int(s)
	# if birth < 2000:
	# 	print('00前')
	# else:
	# 	print('00后')

# 游戏打飞机的框架
	# 加载背景音乐
	# 播放背景音乐(设置单曲循环)
	# 我方飞机诞生
	# interval = 0

	# while True:
	# 	if 用户是否点击了关闭按钮:
	# 		退出程序

	# 	interval += 1
	# 	if interval == 50:
	# 		interval = 0
	# 		小飞机诞生
			
	# 	小飞机移动一个位置
	# 	屏幕刷新

	# 	if 用户鼠标产生移动:
	# 		我反飞机中心位置 = 用户鼠标位置
	# 		屏幕刷新
	# 	if 我反飞机与小飞机发生肢体冲突:
	# 		我反挂,播放装机音乐
	# 		修改我反飞机图案
	# 		停止背景音乐,淡出

# 1~100分输入分数,返回等级  三种方案
	# 1:
	# score = int(input('请输入一个分数'))
	# if 100 >= score >= 90:
	#     print('A')
	# if 90 >= score >= 80:
	#     print('B')
	# if 80 >= score >= 60:
	#     print('C')
	# if 60 >= score >= 0:
	#     print('D')
	# if score < 0 or score > 100:
	#     print('输入错误')

	# 2:

	# 3
	# score = int(input('请输入分数:'))
	# if 100 >= score >= 90:
	#     print('A')
	# elif 90 > score >= 80:
	#     print('B')
	# elif 80 > score >= 60:
	#     print('C')
	# elif 60 > score >= 0:
	#     print('D')
	# else:
	#     print('请重新输入')

# 断言(assert)
	# 单这个关键字后边的条件为假的时候程序自动崩溃并抛出AssertionError
	# 用处就是检查点

# for循环
	# for 目标 in 表达式: 
	# 	循环体

 	# 例:
 	# member['a', 'b', 'c', 'd']
	# for i in member:
	# 	print(i, len(i/membre))