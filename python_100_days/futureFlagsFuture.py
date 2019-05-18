#!usr/bin/python
# -*- coding: utf-8 -*-

"""
@see https://segmentfault.com/a/1190000009819359
python并发：使用 futures 处理并发

从网上下载人口前20的国际的国旗
Future 是 concurrent.futures 模块和 asyncio 包的重要组件。
从Python3.4起，标准库中有两个为Future的类：concurrent.futures.Future 和 asyncio.Future。
这两个Future作用相同。

Future 封装待完成的操作，可放入队列，完成的状态可以查询，得到结果（或抛出异常）后可以获取结果（或异常）。
Future 表示终将发生的事情，而确定某件事情会发生的唯一方式是执行的时间已经排定。
因此只有把某件事交给 concurrent.futures.Executor 子类处理时，才会创建 concurrent.futures.Future 实例。

什么是可调用对象@link https://www.cnblogs.com/z-joshua/p/7756891.html
"""
from concurrent import futures
from futureFlags import save_flag, get_flag, show, main

# 设定ThreadPoolExecutor 类最多使用几个线程
MAX_WORKERS = 3


def download_one(cc):
    """下载一个图片"""
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    cc_list = cc_list[:]
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        to_do = []
        # 用于创建并排定 future
        for cc in sorted(cc_list):
            # submit 方法排定可调用对象的执行时间然后返回一个future，表示这个待执行的操作
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []

        # 用于获取future 结果
        # as_completed 接收一个future 列表，返回值是一个迭代器，在运行结束后产出future
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

        return len(results)


if __name__ == '__main__':
    main(download_many)

"""
从结果可以看到，future 的 repr() 方法会显示状态，前三个 是running 是因为我们设定了三个进程，所以后两个是pendding 状态。
如果将max_workers参数设置为5，结果就会全都是 running。
虽然，使用 future 的脚本比第一个脚本的执行速度快了很多，但由于受GIL的限制，下载并不是并行的。
"""

"""
Executor.map 还有个特性比较有用，那就是这个函数返回结果的顺序于调用开始的顺序是一致的。如果第一个调用称其结果用时10秒，其他调用只用1秒，代码会阻塞10秒，获取map方法返回的生成器产出的第一个结果。
如果不是获取到所有结果再处理，通常会使用 Executor.submit + Executor.as_completed 组合使用的方案。
Executor.submit + Executor.as_completed 这个组合更灵活，因为submit方法能处理不同的可调用对象和参数，而executor.map 只能处理参数不同的同一个可调用对象。此外，传给futures.as_completed 函数的期物集合可以来自不同的 Executor 实例。
"""
