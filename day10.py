# 汉诺塔
	def hanoi(n, x, y, z):
	    if n == 1:
	        print(x, ' -->', z)
	    else:
	        hanoi(n-1, x, z, y)#将前n-1个盘子x移动到y上
	        print(x, ' -->', z)#将最底下的最后一个盘子从x移动到z上
	        hanoi(n-1, y, x, z)#将y上的n-1歌盘子移动到z上

	n = int(input('请输入汉诺塔的层数:'))
	hanoi(n, 'X', 'Y', 'Z')

# dict{'':'',}
	字典,映射类型,pythpn唯一的映射类型
	# 不支持索引
	也可以用,dict()创建

	>>> dict3 = dict((('F', 70), ('i', 105), ('s', 115), ('h', 104)))
	>>> dict3
	{'F': 70, 'i': 105, 's': 115, 'h': 104}

	>>> dict2 = {'陈':'ss', '旭':'jj', '升':'kk'}
	>>> dict2
	{'陈': 'ss', '旭': 'jj', '升': 'kk'}

	dict4 = dict(陈='老爷', 旭='boy')
	>>> dict4
	{'陈': '老爷', '旭': 'boy'}
	>>> dict4['旭'] = '咔咔咔'
	>>> dict4
	{'陈': '老爷', '旭': '咔咔咔'}
	>>> dict4['升'] = '我是新加的'
	>>> dict4
	{'陈': '老爷', '旭': '咔咔咔', '升': '我是新加的'}

# 工厂函数
	str(),list(),tuple(),dict()
	# fromkeys(s[,v])你
	# 先这样吧昨天今天老板找我谈话每次都两个小时,每次都打乱了我的安排
	# 这两天学的太少了一会回家学点吧

