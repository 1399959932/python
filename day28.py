#!/usr/bin/python
进程 vs. 线程
		要实现多任务，通常设计Master-Worker模式，
	Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker

	如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
	如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。

	多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式
	多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

	多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。
	在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂

线程切换
	保存现场	~	CPU寄存器状态、内存页等
	准备新环境	~	恢复上次的寄存器状态，切换内存页等
	才能开始执行


	多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好

计算密集型 vs. IO密集型
	# 是否采用多任务的第二个考虑是任务的类型。
	任务分为计算密集型和IO密集型。

		计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，
	全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。

	# 计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

		IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。
	常见的大部分任务都是IO密集型任务，比如Web应用。

	# IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

异步IO
	充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为/事件驱动模型/，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务

	# 在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。

	对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序


分布式进程
	# 进程（Process）# 把进程内的子任务称为线程（Thread）
	在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
	# multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。


	#关键字lambda表示匿名函数，冒号前面的x表示函数参数

	# 	如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
	# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
	# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
		#day28server.py 	#主进程文件 progess
			请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。

		#day28worker.py #工作文件 threa
			任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。

	我没太明白,
	运行失败                                             │
	┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
	│task_master.py                           │  │  │task_worker.py                        │
	│                                         │     │                                      │
	│  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
	│  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
	│              │                          │  │  │              │                       │
	│              │                          │     │              │                       │
	│              ▼                          │  │  │              │                       │
	│  ┌─────────────────────────────────┐    │     │              │                       │
	│  │QueueManager                     │    │  │  │              │                       │
	│  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
	│  │ │ task_queue │ │ result_queue │ │<───┼──┼──┼──────────────┘                       │
	│  │ └────────────┘ └──────────────┘ │    │     │                                      │
	│  └─────────────────────────────────┘    │  │  │                                      │
	└─────────────────────────────────────────┘     └──────────────────────────────────────┘
                                             │
                                             Network

	# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。
	authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，肯定连接不上。

小结
	Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
	注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。



	loser
	失败了  啊