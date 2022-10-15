import tkinter as tk
from datetime import date
 
main=tk.Tk()
main.title('Procrastination Purger')
main.geometry("1400x800+10+20")
bgcolor = '#B1D4E0'
btncolor = '#145DA0'
textcolor = '#145DA0'
btntextcolor = '#B1D4E0'
main['bg']= bgcolor

def refresh1(txtarea):
    txtarea.destroy()
    txtarea = tk.Text(main,bg = '#E7E7E7', width=33, height=18)
    txtarea.place(x=975, y= 200)

    tf = open("placeholdertext.txt",'r')  
    data = tf.read()
    txtarea.insert(tk.END, data)
    tf.close()
    txtarea.configure(state='disabled',font=("Times", 15))
    
def refresh2(txtarea2):
    txtarea2.destroy()
    txtarea2 = tk.Text(main,bg = '#E7E7E7', width=75, height=10)
    txtarea2.place(x=30, y=250)

    tf = open("placeholdertext.txt",'r')  
    data = tf.read()
    txtarea2.insert(tk.END, data)
    tf.close()
    txtarea2.configure(state='disabled',font=("Times", 15))
    


lbltitle=tk.Label(text="Procrastination Purger",bg = bgcolor, fg= textcolor, font=("Times", 30))
lbltitle.pack(pady=30)
lblnames=tk.Label(text="By Vladislav and Elvin",bg = bgcolor, fg= textcolor, font=("Times", 15))
lblnames.place(x=25,y =10)
btnsettings=tk.Button(text="Settings",bg = btncolor, fg= btntextcolor,font=("Times", 15))
btnsettings.place(x = 1290, y = 10)

lblnextses=tk.Label(text="NEXT SESSION:",bg = bgcolor, fg= textcolor,font=("Times", 20))
lblnextses.place(x = 30, y = 150)
lblnextses=tk.Label(text="Place holder",bg = bgcolor, fg= textcolor,font=("Times", 20))
lblnextses.place(x = 300, y = 150)

lblupses=tk.Label(text="Upcoming Sessions",bg = bgcolor, fg= textcolor,font=("Times", 20))
lblupses.place(x = 1045, y = 150)

lblupdue=tk.Label(text="Upcoming Due Dates",bg = bgcolor, fg= textcolor,font=("Times", 20))
lblupdue.place(x = 300, y = 200)

canvas=tk.Canvas(main,bg = bgcolor,highlightbackground= bgcolor, width=1400, height=20)
canvas.create_line(0,0,1400,0, fill="black", width=10)
canvas.pack()

txtarea = tk.Text(main, bg = '#E7E7E7', width=33, height=18)
txtarea.place(x=975, y=200)

tf = open("placeholdertext.txt",'r')  
data = tf.read()
txtarea.insert(tk.END, data)
tf.close()
txtarea.configure(state='disabled',font=("Times", 15))

txtarea2 = tk.Text(main,bg = '#E7E7E7', width=75, height=10)
txtarea2.place(x=30,y=250)

tfdue = open("placeholdertext.txt",'r')  
data = tfdue.read()
txtarea2.insert(tk.END, data)
tfdue.close()
txtarea2.configure(state='disabled',font=("Times", 15))



btnrefresh1=tk.Button(text="Refresh",bg = btncolor, fg = btntextcolor,font=("Times", 10),command = lambda: refresh1(txtarea))
btnrefresh1.place(x=1308, y=735)

btnrefresh2=tk.Button(text="Refresh",bg = btncolor, fg =btntextcolor,font=("Times", 10),command = lambda: refresh2(txtarea2))
btnrefresh2.place(x=865, y=560)


btndue=tk.Button(text="Add Due Date",bg = btncolor, fg=btntextcolor,font=("Times", 20))
btndue.place(x=30, y=580)

btnava=tk.Button(text="Change Availability",bg = btncolor, fg=btntextcolor,font=("Times", 20))
btnava.place(x=30, y=680)


main.mainloop()
