import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from datetime import date


class DueDate(Toplevel):
    duedates = []

    def __init__(self, main):
        super().__init__(master=main)
        self.create_window()

    def get_duedate(self):
        return self.duedates

    def update_dates(self, entries):
        self.duedates = []
        for en in entries:
            if en.get() == '':
                messagebox.showwarning("Warning", "1. Please do not leave any fields blank")
                self.duedates = []
                break
        if entries[0].get().lower() in "test":
            self.duedates.append(1)
        elif entries[0].get().lower() in "assignment":
            self.duedates.append(0)
        else:
            messagebox.showwarning("Warning", "2. Please enter valid values")
            self.duedates = []
            return self.duedates


        self.duedates.append(entries[1].get())
        self.duedates.append(entries[2].get())
        if not (entries[3].get() == "1" or entries[3].get() == "2" or entries[3].get() == "3"):
            messagebox.showwarning("Warning", "Please enter valid values")
            self.duedates = []
            return self.duedates
        else:
            self.duedates.append(entries[3].get())

    def create_window(self):
        self.title('Add Due Date')
        self.geometry("750x350+10+20")
        bgcolor = '#B1D4E0'
        btncolor = '#145DA0'
        textcolor = '#145DA0'
        btntextcolor = '#B1D4E0'
        self['bg'] = bgcolor

        self.add_labels()
        entries = self.add_entries()
        lbltitle = tk.Label(self, text="Enter Your Assignment/Test", bg=bgcolor, fg=textcolor, font=("Times", 20))
        lbltitle.pack()

        lbltimereminder = tk.Label(self, text="Use MM/DD/YY", bg=bgcolor, fg=textcolor, font=("Times", 15))
        lbltimereminder.place(x=500, y=100)

        lbldiffreminder = tk.Label(self, text="On a scale of 1 to 3", bg=bgcolor, fg=textcolor, font=("Times", 15))
        lbldiffreminder.place(x=500, y=200)

        addbtn = tk.Button(self, text="Add", fg=btntextcolor, bg=btncolor, font=("Times", 10),
                           command=lambda: [self.update_dates(entries), self.destroy()])
        addbtn.place(x=330, y=250)

    def add_labels(self):
        bgcolor = '#B1D4E0'
        textcolor = '#145DA0'
        lblaort = tk.Label(self, text="Assignment or Test?", bg=bgcolor, fg=textcolor, font=("Times", 15))
        lblaort.place(x=20, y=50)

        lbltime = tk.Label(self, text="When is it due?", bg=bgcolor, fg=textcolor, font=("Times", 15))
        lbltime.place(x=20, y=100)

        lblclass = tk.Label(self, text="What class is it for?", bg=bgcolor, fg=textcolor, font=("Times", 15))
        lblclass.place(x=20, y=150)

        lbldifficulty = tk.Label(self, text="How hard is it?", bg=bgcolor, fg=textcolor, font=("Times", 15))
        lbldifficulty.place(x=20, y=200)

    def add_entries(self):
        textbgcolor = '#E7E7E7'
        aortentry = tk.Entry(self, highlightthickness=2, bg=textbgcolor)
        aortentry.place(x=275, y=55)

        timeentry = tk.Entry(self, highlightthickness=2, bg=textbgcolor)
        timeentry.place(x=275, y=105)

        classentry = tk.Entry(self, highlightthickness=2, bg=textbgcolor)
        classentry.place(x=275, y=155)

        diffentry = tk.Entry(self, highlightthickness=2, bg=textbgcolor)
        diffentry.place(x=275, y=205)

        return [aortentry, timeentry, classentry, diffentry]


if __name__ == '__main__':
    addduedates = DueDate([])
    print(addduedates.duedate())
