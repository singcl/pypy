# coding=utf-8

"""
Python 发送邮件
文件名不能为email.py - Python 模块加载机制
"""

from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, Send by Python...', 'plain', 'utf-8')

from_addr = raw_input('From: ')
password = raw_input('Password: ')
smtp_server = raw_input('SMTP server: ')
to_addr = raw_input('To: ')

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
