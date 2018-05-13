#!usr/bin/python
XML
	XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。

DOM vs SAX
		操作XML有两种方法：DOM和SAX。
	DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
	SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
	# 正常情况下，优先考虑SAX，因为DOM实在太占内存。

	start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

	# 举个例子，当SAX解析器读到一个节点时：
	<a href="/">python</a>
	会产生3个事件：
		1.start_element事件，在读取<a href="/">时；
		2.char_data事件，在读取python时；
		3.end_element事件，在读取</a>时。

	#	
	>>> from xml.parsers.expat import ParserCreate
	>>> class DefaultSaxHandler(object):
	    def start_element(self, name, attrs):
	        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

	    def end_element(self, name):
	        print('sax:end_element: %s' % name)

	    def char_data(self, text):
	        print('sax:char_data: %s' % text)

	        
	>>> xml = r'''<?xml version="1.0"?>
	<ol>
	    <li><a href="/python">Python</a></li>
	    <li><a href="/ruby">Ruby</a></li>
	</ol>
	'''
	>>> handler = DefaultSaxHandler()
	>>> parser = ParserCreate()
	>>> parser.StartElementHandler = handler.start_element
	>>> parser.EndElementHandler = handler.end_element
	>>> parser.CharacterDataHandler = handler.char_data
	>>> parser.Parse(xml)
	sax:start_element: ol, attrs: {}
	sax:char_data: 

	sax:char_data:     
	sax:start_element: li, attrs: {}
	sax:start_element: a, attrs: {'href': '/python'}
	sax:char_data: Python
	sax:end_element: a
	sax:end_element: li
	sax:char_data: 

	sax:char_data:     
	sax:start_element: li, attrs: {}
	sax:start_element: a, attrs: {'href': '/ruby'}
	sax:char_data: Ruby
	sax:end_element: a
	sax:end_element: li
	sax:char_data解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。: 

	sax:end_element: ol

	需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。

	# 99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：
	L = []
	L.append(r'<?xml version="1.0"?>')
	L.append(r'<root>')
	L.append(encode('some & data'))
	L.append(r'</root>')
	return ''.join(L)
	# 如果要生成复杂的XML呢？建议你不要用XML，改成JSON。

	解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。

HTMLParser
	如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
	# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
	>>> from html.parser import HTMLParser
	>>> from html.entities import name2codepoint
	>>> class MyHTMLParser(HTMLParser):

	    def handle_starttag(self, tag, attrs):
	        print('<%s>' % tag)

	    def handle_endtag(self, tag):
	        print('</%s>' % tag)

	    def handle_startendtag(self, tag, attrs):
	        print('<%s/>' % tag)

	    def handle_data(self, data):
	        print(data)

	    def handle_comment(self, data):
	        print('<!--', data, '-->')

	    def handle_entityref(self, name):
	        print('&%s;' % name)

	    def handle_charref(self, name):
	        print('&#%s;' % name)

	        
	>>> parser = MyHTMLParser()
	>>> parser.feed('''<html>
	<head></head>
	<body>
	<!-- test html parser -->
	    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
	</body></html>''')
	<html>


	<head>
	</head>

		feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。1
	特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。


	<body>


	<!--  test html parser  -->

	    
	<p>
	Some 
	<a>
	html
	</a>
	 HTML tutorial...
	<br>
	END
	</p>


	</body>
	</html>

		feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
	特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。