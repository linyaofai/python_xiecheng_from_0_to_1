from collections.abc import Coroutine

async def hello(name):
    print('Hello,', name)

if __name__ == '__main__':
    # 生成协程对象，并不会运行函数内的代码
    coroutine = hello("World")

    # 检查是否是协程 Coroutine 类型
    print(isinstance(coroutine, Coroutine))  # True