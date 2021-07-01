from tkinter import *


class Youareshit:
    def __init__(self):
        window = Tk()
        label = Label(window, text='Do youlike this？')
        self.btyes = Button(window, text='no', height=1, width=6)
        self.btno = Button(window, text='yes', height=1, width=6)
        label.place(x=60, y=70)
        self.btyes.place(x=40, y=130)
        self.btno.place(x=120, y=130)
        self.btyes.bind('<Enter>', self.event1)  # 将按钮与鼠标事件绑定，<Enter>是指鼠标光标进入按钮区域
        self.btno.bind('<Enter>', self.event2)
        window.mainloop()

    def event1(self, event):  # 切换按钮文字
        self.btyes['text'] = 'yes'
        self.btno['text'] = 'no'

    def event2(self, event):
        self.btyes['text'] = 'no'
        self.btno['text'] = 'yes'


Youareshit()
window = Tk()
label = Label(window, text='you can not change this')
label.place(x=2, y=80)
button = Button(window, text='就是', command=window.destroy)
button.place(x=80, y=150)
window.mainloop()