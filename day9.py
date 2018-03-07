#!/usr/bin/python

# 递归,
	#原理,函数调用函数
	#有调用函数的行为,有一个正确的返回条件

	import sys 
	sys.setrecursionlimit(10000)	#通过设置递归的深度

	# 写一个求阶乘的函数 5的阶乘 = 1*2*3*4 ,120

	def factorial(n):
    result = n
    for i in range(1,n):
        result *= i

    return result

	number = int(input('请输入一个正整数:'))
	result = factorial(number)
	print('%d 的阶乘是;%d' % (number, result))

	# 递归方式写法

	def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
	# number = int(input('请输入一个正整数:'))
	# result = factorial(number)
	# print('%d 的阶乘是;%d' % (number, result))

# 迭代:
	# 迭代是重复反馈过程的活动，其目的通常是为了逼近所需目标或结果。
	# 每一次对过程的重复称为一次“迭代”，而每一次迭代得到的结果会作为下一次迭代的初始值。

	# 小兔崽子 迭代方法:
	def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('输入有误!')
        return -1

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1


    return n3

	result = fab(60)
	if result != -1:
	    print('总共有%d对小兔崽子诞生' % result)


	# 递归
