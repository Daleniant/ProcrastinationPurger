import tkinter as tk
from Schedule import Schedule
from Due_Date import DueDate
from Availability import Availability
from time_scrapper import TimeScrapper
import pandas

class MainWindow:
    defaults = []
    bgcolor = '#B1D4E0'
    btncolor = '#145DA0'
    textcolor = '#145DA0'
    btntextcolor = '#B1D4E0'

    schedule = []

    def __init__(self):
        avc = Availability()
        time_av = avc.read_file()

        for val in time_av.values:
            self.defaults.append(val[1])

        self.update_schedule()

    def create_window(self):
        main = tk.Tk()
        main.title('Procrastination Purger')
        main.maxsize(width=1400, height=800)
        main.minsize(width=1400, height=800)
        main['bg'] = self.bgcolor

        self.add_labels()
        self.add_text(main)

        main.mainloop()

    def add_labels(self):
        lbltitle = tk.Label(text="Procrastination Purger", bg=self.bgcolor, fg=self.textcolor, font=("Times", 30))
        lbltitle.pack(pady=30)
        lblnames = tk.Label(text="By Vladislav and Elvin", bg=self.bgcolor, fg=self.textcolor, font=("Times", 15))
        lblnames.place(x=25, y=10)

        lblupses = tk.Label(text="Upcoming Sessions", bg=self.bgcolor, fg=self.textcolor, font=("Times", 20))
        lblupses.place(x=1045, y=150)

        lblupdue = tk.Label(text="Upcoming Due Dates", bg=self.bgcolor, fg=self.textcolor, font=("Times", 20))
        lblupdue.place(x=300, y=200)

    def add_text(self, main):
        canvas = tk.Canvas(main, bg=self.bgcolor, highlightbackground=self.bgcolor, width=1400, height=20)
        canvas.create_line(0, 0, 1400, 0, fill="black", width=10)
        canvas.pack()

        txtarea = tk.Text(main, bg='#E7E7E7', width=33, height=18)
        txtarea.place(x=975, y=200)

        sessions = self.get_sessions()
        upcoming = ""
        if sessions:
            for i in range(len(sessions) - 1, 0, -1):
                upcoming += sessions[i] + "\n"
        txtarea.insert(tk.END, upcoming)
        txtarea.configure(state='disabled', font=("Times", 15))

        txtarea2 = tk.Text(main, bg='#E7E7E7', width=75, height=10)
        txtarea2.place(x=30, y=250)

        try:
            tf = open("duedates.txt", 'r')
            data = tf.read()
        except:
            tf = open("duedates.txt", "w")
            data = "No upcoming due dates!"
        txtarea2.insert(tk.END, data)
        tf.close()
        txtarea2.configure(state='disabled', font=("Times", 15))

        btnrefresh1 = tk.Button(text="Refresh", bg=self.btncolor, fg=self.btntextcolor, font=("Times", 10),
                                command=lambda: self.refresh1(txtarea, main))
        btnrefresh1.place(x=1200, y=650)

        btnrefresh2 = tk.Button(text="Refresh", bg=self.btncolor, fg=self.btntextcolor, font=("Times", 10),
                                command=lambda: self.refresh2(txtarea2, main))
        btnrefresh2.place(x=865, y=560)

        btndue = tk.Button(text="Add Due Date", bg=self.btncolor, fg=self.btntextcolor, font=("Times", 20),
                           command=lambda: self.add_due_date(main))
        btndue.place(x=30, y=580)

        btnava = tk.Button(text="Change Availability", bg=self.btncolor, fg=self.btntextcolor, font=("Times", 20),
                           command=lambda: self.change_availability(main))
        btnava.place(x=30, y=680)

    def refresh1(self, txtarea, main):
        txtarea.destroy()
        txtarea = tk.Text(main, bg='#E7E7E7', width=33, height=18)
        txtarea.place(x=975, y=200)

        self.update_schedule()

        sessions = self.get_sessions()
        upcoming = ""
        if sessions:
            for i in range(len(sessions) - 1, 0, -1):
                upcoming += sessions[i] + "\n"
        txtarea.insert(tk.END, upcoming)
        txtarea.configure(state='disabled', font=("Times", 15))


    def refresh2(self, txtarea2, main):
        txtarea2.destroy()
        txtarea2 = tk.Text(main, bg='#E7E7E7', width=75, height=10)
        txtarea2.place(x=30, y=250)
        
        try:
            tf = open("duedates.txt", 'r')
            data = tf.read()
        except:
            tf = open("duedates.txt", "w")
            data = "No upcoming due dates!"
        txtarea2.insert(tk.END, data)
        tf.close()
        txtarea2.configure(state='disabled', font=("Times", 15))

    def add_due_date(self, main):
        due_screen = DueDate(main)
        due_screen.wait_window()

        duedate = due_screen.get_duedate()
        day = duedate[1]
        course = duedate[2]
        hours = 3 * int(duedate[3]) * (2 ** duedate[0])

        f = open("duedates.txt", "a+")
        f.write(day + ' ' + course + '\n')
        f.close()

        self.schedule.add_due_date(day, course, hours)
        self.update_schedule()

    def change_availability(self, main):
        scrapper = TimeScrapper(self.defaults, main)
        scrapper.wait_window()

        time = scrapper.get_time()
        avc = Availability()
        avc.update_file(time)

        return scrapper.get_time()

    def get_sessions(self):
        sessions = []
        schedule = self.schedule.get_schedule()
        if schedule is pandas.DataFrame.empty:
            return []

        for i in schedule.index:
            session_str = schedule.at[i, 'Date'] + ", from "
            session_str = session_str + schedule.at[i, 'Time'] + ", class: "
            session_str = session_str + schedule.at[i, "Course"]

            sessions.append(session_str)

        return sessions

    def update_schedule(self):
        avc = Availability()
        df = avc.read_file()

        time_av = []
        for i in df.index:
            time_av.append(df.at[i, 'Time'])
        print(time_av)

        self.schedule = Schedule(time_av)


if __name__ == '__main__':
    wind = MainWindow()
    wind.create_window()
