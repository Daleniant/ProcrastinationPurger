import tkinter as tk
from datetime import date

class DueDate:
    duedates = []
    def __init__(self, duedates):
        self.duedates = []
        self.create_window()
    def duedate(self):
        return self.duedates
    
    def is_valid_date(self,year, month, day):
        today = date.today()
        if year == int(today.strftime("%y")):
            if month == int(today.strftime("%m")):
                if day <= int(today.strftime("%d")):
                    return False
            elif month < int(today.strftime("%y")):
                return False
        elif year < int(today.strftime("%y")):
            return False
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year%4==0 and (year%100 != 0 or year%400==0):
            day_count_for_month[2] = 29
        return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])
    
    def update_dates(self, entries):
        self.duedates = []
        for en in entries:
            if (en.get() == ''):
                tk.messagebox.showwarning("Warning","Please do not leave any fields blank")
                self.duedates = []
                break
        if (entries[0].get() == "Test") or (entries[0].get() == "test"):
            self.duedates.append(1)
        elif (entries[0].get() == "Assignment") or (entries[0].get() == "assignment"):
            self.duedates.append(0)
        else:
            tk.messagebox.showwarning("Warning","Please enter valid values")
            self.duedates = []
            return self.duedates
        a,b,c = entries[1].get().split('/')
        if not self.is_valid_date(int(c),int(a),int(b)):
            tk.messagebox.showwarning("Warning","Please enter valid values")
            self.duedates = []
            return self.duedates

        else:
            self.duedates.append(entries[1].get())
        self.duedates.append(entries[2].get())
        if not (entries[3].get() =="1" or entries[3].get() == "2" or entries[3].get() =="3"):
            tk.messagebox.showwarning("Warning","Please enter valid values")
            self.duedates = []
            return self.duedates
        else:
            self.duedates.append(entries[3].get())

    def create_window(self):
        window=tk.Tk()
        window.title('Add Due Date')
        window.geometry("750x350+10+20")
        bgcolor = '#B1D4E0'
        btncolor = '#145DA0'
        textcolor = '#145DA0'
        btntextcolor = '#B1D4E0'
        textbgcolor= '#E7E7E7'
        window['bg']= bgcolor
        
        labels = self.add_labels()
        entries = self.add_entries()
        lbltitle=tk.Label(text="Enter Your Assignment/Test",bg = bgcolor, fg= textcolor, font=("Times", 20))
        lbltitle.pack()

        lbltimereminder=tk.Label(text="Use MM/DD/YY",bg = bgcolor, fg= textcolor, font=("Times", 15))
        lbltimereminder.place(x=500, y=100)
        
        lbldiffreminder=tk.Label(text="On a scale of 1 to 3",bg = bgcolor, fg= textcolor, font=("Times", 15))
        lbldiffreminder.place(x=500, y=200)
        
        addbtn = tk.Button(text="Add", fg=btntextcolor, bg = btncolor, font=("Times", 10), command=lambda: [self.update_dates(entries),window.destroy()])
        addbtn.place(x=330, y=250)
        
        window.mainloop()
        
    def add_labels(self):
        bgcolor = '#B1D4E0'
        textcolor = '#145DA0'
        lblaort=tk.Label(text="Assignment or Test?",bg = bgcolor, fg= textcolor, font=("Times", 15))
        lblaort.place(x=20, y=50)
        
        lbltime=tk.Label(text="When is it due?",bg = bgcolor, fg= textcolor, font=("Times", 15))
        lbltime.place(x=20, y=100)

        lblclass=tk.Label(text="What class is it for?",bg = bgcolor, fg= textcolor, font=("Times", 15))
        lblclass.place(x=20, y=150)

        lbldifficulty=tk.Label(text="How hard is it?",bg = bgcolor, fg= textcolor, font=("Times", 15))
        lbldifficulty.place(x=20, y=200)
        
        return [lblaort,lbltime,lblclass,lbldifficulty]
    
    def add_entries(self):
        textbgcolor= '#E7E7E7'
        aortentry= tk.Entry(highlightthickness=2,bg = textbgcolor)
        aortentry.place(x = 275, y= 55)
        
        timeentry= tk.Entry(highlightthickness=2,bg = textbgcolor)
        timeentry.place(x = 275, y= 105)

        classentry= tk.Entry(highlightthickness=2,bg = textbgcolor)
        classentry.place(x = 275, y= 155)

        diffentry= tk.Entry(highlightthickness=2,bg = textbgcolor)
        diffentry.place(x = 275, y= 205)

        return [aortentry,timeentry,classentry,diffentry]

if __name__ == '__main__':
  addduedates = DueDate([])
  print(addduedates.duedate())
    