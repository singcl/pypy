# coding: utf-8

"""蓄水池算法实现随机抽样

随机抽样问题
"""
import random


class ReservoirSimple(object):
    def __init__(self, size):
        self._size = size
        self._counter = 0
        self._sample = []

    def feed(self, item):
        self._counter += 1
        # 第i个元素（i <= k）直接进入池子中
        if len(self._sample) < self._size:
            self._sample.append(item)
            return self._sample
        # 第i个元素 (i > k) 以 k/i的概率进入池子中
        rand_int = random.randint(1, self._counter)
        if rand_int <= self._size:
            self._sample[rand_int - 1] = item
        return self._sample
