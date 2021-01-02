from tkinter import Tk, Label, Button, Text
 
window = Tk()
 
window.title('m4注册机')
 
window.geometry('300x100')  # 这里的乘是小x
 
l = Label(window, text="来看看是个啥", font=(10))
l.pack()

def insert_point(): # 在鼠标焦点处插入输入内容
    check_value = "kXy^rO|*yXo*m\kMuOn*+"
    key_value = ""
    for i in range(len(check_value)):
        key_value += chr(ord(check_value[i]) - 0xA)
    t.insert('insert', key_value)

b1 = Button(window, text='insert point', width=10,
               height=1, command=insert_point)
b1.pack()
 
t = Text(window, width=25, height=1)
t.pack()

window.mainloop()

