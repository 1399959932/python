#!use/bin/python
# print('hello, world')

# 函数
# 	def func():
# 	求和符号∑

# 求圆的面积
	# import math # 导入math模块，下面用到pi
	# list1 = [12.34, 9.08, 73.1] # 将3个不同面积的圆半径定义成一个lis

	# def area_sum(i): # 定义area_sum函数，套用圆的面积计算公式
	# 	area = math.pi * i * i
	# 	print(area) # 打印圆的面积

	# for iii in list1:# 将列表的3个半径循环
	# 	print(iii)  # 一次将值给area_sum函数

	# area_sum(list1[2]) #求圆的面积

# python内置函数
	abs()	只有一个参数,求其绝对值
	hex(i)	把一个整数转换成十六进制表示的字符串

# 调用函数:
	# 把函数赋值给一个变量
		a = abs # 变量a指向abs函数
		a(-1) # 所以也可以通过a调用abs函数
	# 直接调用:
		abs(i) #函数名传参

# 简洁并符合要求是第一生产力
	n1 = hex(n1)
	n2 = hex(n2)
	print(str(n1), str(n2))

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。