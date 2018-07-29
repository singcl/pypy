#!/usr/bin/env python
# coding: utf-8

"""GUI"""
# from Tkinter import *
import Tkinter as Tk


class Application(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.pack()
        self.helloLabel = Tk.Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Tk.Button(self, text='退出', command=self.quit)
        self.quitButton.pack()


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 设置成窗体大小
app.master.geometry('500x300+500+200')
# 主消息循环:
app.mainloop()
