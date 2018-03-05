#!C:/Users/JK-chenxs/AppData/Local/Programs/Python
# print('hello,world')
# range()
# 	语法:
# 		range([start,] stop[, step=1])
# 	[]内的两个参数可选,step=1表示第三个参数的值默认值是1
# 	作用:
# 		生成一个从start参数的值开始到stop参数的值结束的数字序列
# range(5)
# list(range(5))
# print(1)
# for i in range(5):
# 	print(i)
# for a in range(1, 6, 2):
# 	print(a)

# break语句 终止循环
	# bingo = '陈老爷'
	# want = input('你叫我什么:')
	# while True:
	# 	if want == bingo:
	# 		break
	# 	want = input('我不是:')
	# print('以后请叫我陈老爷')
	# print('不要问我为什么')

# continue语句 终止本轮循环,并开始下一句循环
# for i in range(10):
# 	if i%2 != 0: #判断i不是偶数的话
# 		print(i)
# 		continue
# 	i += 2
# 	print(i)

# list 列表,可以存在不同数据类型的数组
# 添加:
# 	list.append('')
# 	list.extend(['', ''])
# 	list.insert(i, '')

# 删除:
	# list.pop() 3最后一个
	# list.pop(i)
	# list.remove('var1') var1 = 元素名字

	# del 属于语句
	# del list[i]删除索引i的元素

# 列表分片(切片) Slice 一次次获取多个元素 'i:i'
# 	list[1:3]  3 - 1 得到两个元素, 0 - 3 得到三个
# 	list[:1]  得到(var0,)
# 	list[i:]  得到(vari,var+=1) 右边包括i
# python的比较是从0开始比较只要有一个错就返回F,对的继续知道全对返回T反之F
# 字符串用'+'拼接 (数据类型需要相同),用'*'换行
# count('元素')统计元素个数
# index()查询元素索引,可指定位置
# reverse()反转元素排列
# sort()元素从小到大排列
# sort(reverse=True)从大到小排列

# tuple: 元祖 tuple 与 list相似 , 但是不能改变元素
# 但 当tuple内部镶入list, list内部的元素可被改变
	# q = (1, 2, 3, 4)
	# q = q[:2] + (2,) + q[2:]
	# 返回结果(1, 2, 3, 2, 4)
	# 用切片操作可以使q分割成两个list,在添加元祖('',),在重新组合一个元祖并替换

# 字符串
# 字符串处理方法:
	capitalize() 字符串首字符大写
	casefole()  把整个字符串的所有字符小写
	center(width) 将字符串居中,并使用空格填充到长度width的新字符串
	count(sub, [start[,end]]) 返回sub在字符串里边出现的次数,start
		和end参数表示范围,可选
	encode(encoding='utf-8',errors='strict')
		以encoding指定的编码格式对字符串进行编码
	endwidth(sub, [start[,end]]) 检查字符串是不是已sub结束的返回布尔
	expandtabs([tabsize=8])把字符串中的tab符号(\t)转行为空格,如不制定参数
	默认的空格数是tabsize = 8
	find(sub, [start[,end]])检测sub是否包含在字符串中,如果有则返回索引值,否则返回-1
	index(sub, [start[,end]])同find方法,如果sub不在string中则会产生一个异常

	isalnum()如果字符串中至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False
	isalpha()如果字符串中至少有一个字符并且所有字符都是字母则返回True,否则返回False
	isdecimal()如果字符串中包含十进制主返回True,否则False
	isdigit()如果字符串只包含数字则返回True,否则False
	islower()如果字符串中至少包含一个区分大小写的字符,并且这些字符都是小写,则返回True,否则False
	isnumeric()如果字符串中只包含数字字符则返回True,否则False
	isspace()如果字符串中只包含空格则返回True,否则False
	istitle()如果字符串式标题化(所有的单词都是以大写开始,其余字母均小写)则返回True,否则False
	issupper()如果字符串中至少包含一个区分大小写的字符,并且这些支付都是大写则返回True
		,否则False

	join(sub)以字符串作为分隔符,插入所有字符之间
	ijust(width)返回一个左对齐的字符串,并使用空格填充width的新字符串
	lower()转换字符串中所有大写字符为小写
	lstrip()去掉字符串中左边的所有空格
	rstrip()去掉末尾(右边)的空格
	partition(sub)找到子字符串sub,吧字符串分层一个3元组(pre_sub,sub,fol_sub)
	如果字符串中不包括sub则返回('原字符串', '', '')
	replace(old,new[,count])把old子字符串替换成new子字符串,如果指定count,这不超过count次数
	rfind(sub, [start[,end]])同find,重右开始查找
	rindex(sub, [start[,end]])同find,从右开始查找

	split(sep=None, maxsplit=-1)不带参数默认是以空格为分隔符切片字符串
		返回切片后的字符串拼接的list
	splitlines([keepends(])按照'\n'分割
	startwidth(prefix, [start[,end]])检查字符串是否已prefix开头,是则返回True...
	strip([chars])删除字符串前边和后边所有的空格, chars参数可以定制删除的字符,可选
	swaocase()反转字符串中的大小写
	title()返回标题化(首字母大写,其余小写)的字符串
	translate(table)根据table的规则(可以由str.maketrans(a,b)定制)转化字符串中的字符
		# str3 = 'ssssssssssssswwwwwwwwwwsasdasdsad'
		# str3.translate(str.maketrans('s', 'l'))
	upper()转换字符串中所有小写字符为大写
	zfill(width)返回长度为width的字符串,原字符串右对齐,前边用0填充
