#!/usr/bin/python
contextlib
	在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。
	正确关闭文件资源的一个方法是使用try...finally：
	#
	try:
	    f = open('/path/to/file', 'r')
	    f.read()
	finally:
	    if f:
	        f.close()

	Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭
	#等于上
	>>> with open('path/to/file', 'r') as f:
	f.read()

		并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
	实现上下文管理是通过__enter__和__exit__这两个方法实现的
	>>> class Query(object):

	    def __init__(self, name):
	        self.name = name

	    def __enter__(self):
	        print('Begin')
	        return self

	    def __exit__(self, exc_type, exc_value, traceback):
	        if exc_type:
	            print('Error')
	        else:
	            print('End')

	    def query(self):
	        print('Query info about %s...' % self.name)

	#调用query类     
	>>> with Query('ROnin') as q:
		q.query()

		
	Begin
	Query info about ROnin...
	End

@contextmanager
	编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法
	#等于上的query类
	>>> from contextlib import contextmanager
	>>> class Query(object):

	    def __init__(self, name):
	        self.name = name

	    def query(self):
	        print('Query info about %s...' % self.name)

	        
	>>> @contextmanager
	def create_query(name):
	    print('Begin')
	    q = Query(name)
	    yield q
	    print('End')

	    
	>>> with create_query('Bob') as q:
	    q.query()

	    
	Begin
	Query info about Bob...
	End

	@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
	
	Decorator, 装饰器
		在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
	生成器, generator
    	一边循环一边计算的机制，称为生成器：generator

    # 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
    >>> @contextmanager
	def tag(name):
		print("<%s>" % name)	#1
		yield
		print("</%s>" % name)	#3

		
	>>> with tag("h1"):	#2
		print("hello")
		print("time")

		
	<h1>
	hello
	time
	</h1>
	>>> with tag("h1"):
		print("hello")
		print('time')

		
	<h1>
	hello
	time
	</h1>

	#代码的执行顺序
		with语句首先执行yield之前的语句，因此打印出<h1>；
		yield调用会执行with语句内部的所有语句，因此打印出hello和world；
		最后执行yield之后的语句，打印出</h1>。

	@contextmanager让我们通过编写generator来简化上下文管理

@closing
		如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用
	closing()来把该对象变为上下文对象
	# 例如，用with语句使用urlopen()：
	>>> from contextlib import closing
	>>> from urllib.request import urlopen
	>>> with closing(urlopen('https://www.python.org')) as page:
		for line in page:
			print(line)

			
	b'<!doctype html>\n'
	...

	closing也是一个经过@contextmanager装饰的generator，
	#ji
	@contextmanager
	def closing(thing):
	    try:
	        yield thing
	    finally:
	        thing.close()
	# 它的作用就是把任意对象变为上下文对象，并支持with语句

urllib
	urllib提供了一系列用于操作URL的功能

GET
	urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
	# 如，对知乎的一个URLhttps://www.zhihu.com/question/61684436/answer/388307186进行抓取，并返回响应：
	>>> from urllib import request
	>>> with request.urlopen('https://www.zhihu.com/question/61684436/answer/388307186') as f:
		data = f.read()
		print('Status:', f.status, f.reason)
		for k, v in f.getheaders():
			print('%s: %s' % (k, v))
		print('Data:', data.decode('utf-8'))

	# 可以看到HTTP响应的头和JSON数据：	
	Status: 200 OK
	Date: Sat, 12 May 2018 12:01:11 GMT
	Content-Type: text/html; charset=utf-8
	Content-Length: 40313
	Connection: close
	Set-Cookie: tgw_l7_route=c919f0a0115842464094a26115457122; Expires=Sat, 12-May-2018 12:16:11 GMT; Path=/
	Vary: Accept-Encoding
	Vary: Accept-Encoding
	Pragma: no-cache
	Expires: Fri, 02 Jan 2000 00:00:00 GMT
	X-Frame-Options: DENY
	Cache-Control: private,no-store,max-age=0,no-cache,must-revalidate,post-check=0,pre-check=0
	Content-Security-Policy: default-src * blob:;img-src * data: blob:;frame-src 'self' *.zhihu.com getpocket.com note.youdao.com safari-extension://com.evernote.safari.clipper-Q79WDW8YH9 weixin: zhihujs: v.qq.com v.youku.com www.bilibili.com *.vzuu.com captcha.guard.qcloud.com;script-src 'self' *.zhihu.com *.google-analytics.com zhstatic.zhihu.com res.wx.qq.com 'unsafe-eval' unpkg.zhimg.com unicom.zhimg.com captcha.gtimg.com captcha.guard.qcloud.com blob:;style-src 'self' *.zhihu.com unicom.zhimg.com 'unsafe-inline' captcha.gtimg.com;connect-src * wss:
	Set-Cookie: _xsrf=81e9f182-c820-4745-af57-0b15dc024d57; path=/; domain=.zhihu.com
	X-Backend-Server: heifetz.heifetz.9c9930cc---10.70.4.3:31018[10.70.4.3:31018]
	Server: ZWS
	Data: <!doctype html>
	...
	</html>

	如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
	# 例如，模拟iPhone 6去请求豆瓣首页：
	from urllib import request

	req = request.Request('http://www.douban.com/')
	req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	with request.urlopen(req) as f:
	    print('Status:', f.status, f.reason)
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', f.read().decode('utf-8'))
	# 这样豆瓣会返回适合iPhone的移动版网页：
	<!DOCTYPE html>
	<html itemscope itemtype="http://schema.org/WebPage">
    <head>
        <meta charset="UTF-8">
        <title>豆瓣(手机版)</title>

POST
	如果要以POST发送一个请求，只需要把参数data以bytes形式传入
	#我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
	from urllib import request

	req = request.Request('http://www.douban.com/')
	req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	with request.urlopen(req) as f:
	    print('Status:', f.status, f.reason)
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', f.read().decode('utf-8'))
	这样豆瓣会返回适合iPhone的移动版网页：

	...
	    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
	    <meta name="format-detection" content="telephone=no">
	    <link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
	...
	Post
	如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

	我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：

	from urllib import request, parse

	print('Login to weibo.cn...')
	email = input('Email: ')
	passwd = input('Password: ')
	login_data = parse.urlencode([
	    ('username', email),
	    ('password', passwd),
	    ('entry', 'mweibo'),
	    ('client_id', ''),
	    ('savestate', '1'),
	    ('ec', ''),
	    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
	])

	req = request.Request('https://passport.weibo.cn/sso/login')
	req.add_header('Origin', 'https://passport.weibo.cn')
	req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

	with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	    print('Status:', f.status, f.reason)
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', f.read().decode('utf-8'))
	如果登录成功，我们获得的响应如下：
	
    
	Status: 200 OK
	Server: nginx/1.6.1
	Date: Sat, 12 May 2018 13:00:23 GMT
	Content-Type: text/html
	Transfer-Encoding: chunked
	Connection: close
	Vary: Accept-Encoding
	Cache-Control: no-cache, must-revalidate
	Expires: Sat, 26 Jul 1997 05:00:00 GMT
	Pragma: no-cache
	Access-Control-Allow-Origin: https://passport.weibo.cn
	Access-Control-Allow-Credentials: true
	DPOOL_HEADER: lich78
	Set-Cookie: login=81272d1749a34b78139b2ac96fdac143; Path=/
	Data: {"retcode":50011007,"msg":"\u8bf7\u8f93\u5165\u7528\u6237\u540d","data":{"errline":318}}
	如果登录失败，我们获得的响应如下：

	...
	Data: {"retcode":50011015,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"example@python.org","errline":536}}

Handler
	如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
	proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
	proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
	opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
	with opener.open('http://www.example.com/login.html') as f:
	    pass

小结
	urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。