# coding: utf-8
"""Python 模块作为脚本执行示例"""

import sys
from fibo import fibo2

if __name__ == "__main__":
    x = fibo2(int(sys.argv[1]))
    print (x)
