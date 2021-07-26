import tkinter as ui
import time

root = ui.Tk()
def clock():
    hours=time.strftime('%H')
    minutes=time.strftime('%M')
    seconds=time.strftime('%S')
    am_pm=time.strftime('%p')
    maintime=hours+":"+minutes+":"+seconds+" "+am_pm
    count.config(text=maintime)





root.title('Digital Clock')
root.configure(bg='BLACK')
count=ui.Label(root,text='00:00:00',font=('straight','50'),bg='BLACK',fg='RED')
count.pack()
clock()
root.mainloop()
