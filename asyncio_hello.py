# coding: utf-8

"""
简单的asyncio hello world
"""

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world")
    # 异步调用asyncio.sleep():
    r = yield from asyncio.sleep(2)
    print("Hello singcl")

# @asyncio.coroutine
def main(co):
    yield from co()

if __name__ == '__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(main(hello))
    loop.close()
