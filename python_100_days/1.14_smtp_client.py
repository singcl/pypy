"""
就像我们可以用HTTP（超文本传输协议）来访问一个网站一样，发送邮件要使用SMTP（简单邮件传输协议），
SMTP也是一个建立在TCP（传输控制协议）提供的可靠数据传输服务的基础上的应用级协议，它规定了邮件的发送者如何跟发送邮件的服务器进行通信的细节，
而Python中的smtplib模块将这些操作简化成了几个简单的函数。
"""
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'qipabaiduid002@163.com'
    receivers = ['1276837689@qq.com']

    message = MIMEText("用Python发送邮件示例", 'plain', 'utf-8')
    message['From'] = Header('singcl', 'utf-8')
    message['To'] = Header('Singcl2 qq', 'utf-8')
    message['Subject'] = Header('Python实验邮件', 'utf-8')
    smtper = SMTP('smtp.126.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, input("请输入密码:"))
    smtper.sendmail(sender, receivers, message.as_string())
    print("邮件发送完成！")

if __name__ == "__main__":
    main()
