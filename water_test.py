# coding: utf-8
"""随机抽样测试用例
"""

import unittest
from collections import Counter
from water import ReservoirSimple


class TestMain(unittest.TestCase):
    samples = []
    for i in range(10000):
        sample = []
        rs = ReservoirSimple(3)
        for item in range(1, 11):
            sample = rs.feed(item)
        samples.extend(sample)
    r = Counter(samples)
    print r


if __name__ == "__main__":
    unittest.main()
