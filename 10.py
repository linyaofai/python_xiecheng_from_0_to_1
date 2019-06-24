# event_loop 事件循环：程序开启一个无限的循环，程序员会把一些函数（协程）注册到事件循环上。当满足事件发生的时候，调用相应的协程函数。
#
#
# coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
#
#
# future 对象： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
#
#
# task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将 coroutine 和 Future 联系在一起，将 coroutine 封装成一个 Future 对象。
#
#
# async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。其作用在一定程度上类似于yield。


# 协成完成的工作流程
# 1.创建协成对象
# 2.创建事件循环容器
# 3.将协成对象转换为task任务
# 4.将task任务扔进循环事件

import asyncio

async def hello(name):
    print('Hello,', name)

# 定义协程对象
coroutine = hello("World")

# 定义事件循环对象容器
loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)

# 将协程转为task任务
task = loop.create_task(coroutine)

# 将task任务扔进事件循环对象中并触发
loop.run_until_complete(task)