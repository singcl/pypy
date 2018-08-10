# coding=utf-8

import sys
# type = sys.getfilesystemencoding()  # 获取文件的默认编码方式
reload(sys)
sys.setdefaultencoding('utf-8')

"""Python中文编码问题
1.windows系统终端显示默认编码为：GBK
2.print 语句和 print 函数 支持直接 unicode 显示,所以中文前加 u 辨识就可以正常显示
3.input函数, raw_input函数 不支持直接unicode显示,所以必须手动 encode为 gbk

如果在文档开头设置：
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
那么中文字符串我们就只需要encode('gbk)，不需要先decode('utf-8'),否则：
str.decode('utf-8').encode('gbk')

gbk 是无法编码emoji 表情的，所以我们直接显示emoji 的原始unicode编码
"😰".encode('unicode_escape')
"""

# print 支持直接 unicode 显示
print (u'-----------------我是Jankin--------------')
# input, raw_input 不支持直接unicode显示,所以必须手动 encode 为 gbk
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字:".encode('gbk'))
# temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字:".decode('utf-8').encode('gbk'))
guess = int(temp)
if guess == 8:
    print (u"我草，你是小甲鱼心里的蛔虫吗？! ")
    print (u"哼，猜中了也没有奖励！")
else:
    if guess > 8:
        print (u"哥，大了大了~~~")
    else:
        print (u"嘿，小了，小了~~~")
# 'gbk' codec can't encode character u'\ud83d'
# gbk 是无法编码emoji 表情的，所以我们直接显示emoji 的原始unicode编码
print ("游戏结束，不玩啦".encode('gbk') + "😰".encode('unicode_escape'))
