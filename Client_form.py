#-*- coding:utf-8 -*-
'''
Created on 01 06 2013

@author: ivan
'''
from Tkinter import *
from client import *
from threading import Thread

class ChatForm:
    def __init__(self):
        self.w = root.winfo_screenwidth()
        self.h = root.winfo_screenheight()
        self.x = 225
        self.y = 130
        
        #place window into center of the screen
        root.geometry("%dx%d+%d+%d" % (self.x, self.y, self.w/2-self.x/2, self.h/2-self.y/2))
        
        self.login = StringVar()
        self.password = StringVar()
        
        Label(root, text="Login:").place(x=25, y=25)        
        self.text1 = Entry(root, textvariable=self.login)
        self.text1.place(x=100, y=25, width = 100)
        
        def OnClick(ev):
            sender.Send(self.text1.get())
        btn1 = Button(root, text='Send Message')
        btn1.place(x=25, y=85, width = 175)
        btn1.bind('<Button-1>', OnClick)
        
      
        
        
        

        

root = Tk()
root.title("SoftDev Chat")
Form1 = ChatForm()
receiver=Client()
receiver.Connect("127.0.0.1", 81)
Thread(target=receiver.StartReceive).start()
sender=Client()
sender.Connect("127.0.0.1", 82)
root.mainloop()
receiver.Disconnect()
sender.Disconnect()
