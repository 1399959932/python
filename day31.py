#!usr/bin/python
base64
	Base64是一种用64个字符来表示任意二进制数据的方法
	# Base64是一种最常见的二进制编码方法
	# 对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
								64
	24							24					24
	6666  6666	6666 6666	6666  6666	6666  6666	6666  6666	6666 6666

		我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。
	Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示

	# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

	# Python内置的base64可以直接进行base64的编解码：
	>>> import base64
	>>> base64.b64encode(b'binart\x00string')
	b'YmluYXJ0AHN0cmluZw=='
	>>> base64.b64encode(b'binart\Chen Ronin')
	b'YmluYXJ0XENoZW4gUm9uaW4='
	>>> base64.b64encode(b'Name\Chen Ronin')
	b'TmFtZVxDaGVuIFJvbmlu'
	>>> base64.b64encode(b'TmFtZVxDaGVuIFJvbmlu')
	b'VG1GdFpWeERhR1Z1SUZKdmJtbHU='
	>>> base64.b64decode(b'TmFtZVxDaGVuIFJvbmlu')
	b'Name\\Chen Ronin'

	标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
	>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
	b'abcd++//'
	>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
	b'abcd--__'
	>>> base64.urlsafe_b64encode(b'abcd--__')
	b'YWJjZC0tX18='
	>>> base64.urlsafe_b64decode('abcd--__')
	b'i\xb7\x1d\xfb\xef\xff'

	Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

	Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。


	由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
	# 标准Base64:
	'abcd' -> 'YWJjZA=='
	# 自动去掉=:
	'abcd' -> 'YWJjZA'
	# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了

	Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

struct
	由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。

	在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，得配合位运算符这么写：
	>>> n = 20180510
	>>> b1 = (n & 0xff000000) >> 24
	>>> b2 = (n & 0xff0000) >> 16
	>>> b2 = (n & 0xff00) >> 8
	>>> b3 = (n & 0xff00) >> 8
	>>> b4 = n & 0xff
	>>> bs = bytes([b1, b2, b3, b4])
	>>> bs
	b'\x01\xee\xee\x1e'
	#很麻烦, 而且对float没有办法

	SO, python的struct模块来解决bytes和其他二进制数据类型的转换
	# struct的pack函数把任意数据类型变成bytes：
	>>> import struct
	>>> struct.pack('>I', 20180510)
	b'\x013\xee\x1e'
	# pack的第一个参数是处理指令，'>I'的意思是：
	# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
	# 后面的参数个数要和处理指令一致。

	unpack把bytes变成相应的数据类型：
	>>> struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
	(4042322160, 32896)
	# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。


	Windows的位图文件（.bmp）是一种非常简单的文件格式，
	BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
	>>> s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

	两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
	一个4字节整数：表示位图大小；
	一个4字节整数：保留位，始终为0；
	一个4字节整数：实际图像的偏移量；
	一个4字节整数：Header的字节数；
	一个4字节整数：图像宽度；
	一个4字节整数：图像高度；
	一个2字节整数：始终为1；
	一个2字节整数：颜色数。

	>>> struct.unpack('<ccIIIIIIHH', s)	#用unpack读取：
	(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)	#结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。
	# 我的失败了 困了 以后再议