#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import Tkinter

import tkinter as tk

tk._test()  # 测试 tkinter 是否正常工作

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('LiangBa Main Window')

# resize root window
top_win.geometry('800x600')

# generate a label
lbl_hello = tk.Label(top_win, text='Hello world!', bg='blue',
             font=('Arial', 12), width=30, height=2)
# put lable onto window
#lbl_hello.pack()
lbl_hello.place()

# 进入消息循环
top_win.mainloop()
