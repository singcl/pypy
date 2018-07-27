# coding: utf-8

"""Python 异常

异常处理
"""
import sys

while True:
    try:
        x = int(raw_input('Please enter a number'))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

# 多个except子句


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
