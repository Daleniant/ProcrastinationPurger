import tkinter as tk

class TimeScrapper:
  time_availability = []

  def __init__(self, defaults):
     self.time_availability = defaults
     self.create_window()

  def get_time(self):
     return self.time_availability

  def update_time(self, entries):
     self.time_availability = []
     for en in entries:
        self.time_availability.append(en.get())

  def create_window(self):
     window = tk.Tk()
     window['bg']= '#B1D4E0'
     labels = self.add_labels()
     entries = self.add_entries()

     lblex = tk.Label(text="Example: 09:00-13:00 (Don't put more than one time interval)", fg='#145DA0', bg = '#B1D4E0',
     font=("Times", 10))
     lblex.place(x=325, y=75)
     lblex = tk.Label(text="Leave the box as 0 if you are not free that day", fg='#145DA0', bg = '#B1D4E0',
     font=("Times", 10))
     lblex.place(x=325, y=125)

     btn = tk.Button(text="Save", fg='#B1D4E0',bg ='#145DA0', font=("Times", 10), command=lambda: [self.update_time(entries),window.destroy()])
     btn.place(x=205, y=425)

     lbl = tk.Label(text="Input your time availability for studying (In 24h format)", fg='#145DA0', bg = '#B1D4E0',
     font=("Times", 20))
     lbl.place(x=50, y=120)

     lbl.pack()

     window.title('Time Availability')
     window.geometry("800x500+10+20")
     window.mainloop()

  def add_labels(self):
     lblmon = tk.Label(text="Monday:", fg='#145DA0', bg = '#B1D4E0', font=("Times", 10))
     lblmon.place(x=50, y=75)

     lbltues = tk.Label(text="Tuesday:", fg='#145DA0', bg = '#B1D4E0', font=("Times", 10))
     lbltues.place(x=50, y=125)

     lblwed = tk.Label(text="Wednesday:", fg='#145DA0',bg = '#B1D4E0', font=("Times", 10))
     lblwed.place(x=50, y=175)

     lblthurs = tk.Label(text="Thursday:", fg='#145DA0',bg = '#B1D4E0', font=("Times", 10))
     lblthurs.place(x=50, y=225)

     lblfri = tk.Label(text="Friday:", fg='#145DA0', bg = '#B1D4E0',font=("Times", 10))
     lblfri.place(x=50, y=275)

     lblsat = tk.Label(text="Saturday:", fg='#145DA0',bg = '#B1D4E0', font=("Times", 10))
     lblsat.place(x=50, y=325)

     lblsun = tk.Label(text="Sunday:", fg='#145DA0',bg = '#B1D4E0', font=("Times", 10))
     lblsun.place(x=50, y=375)

     return [lblmon, lbltues, lblwed, lblthurs, lblfri, lblsat, lblsun]

  def add_entries(self):
     time_mon = tk.Entry(highlightthickness=2,bg ='#E7E7E7')
     time_mon.place(x=150, y=75)
     #time_mon.config(highlightbackground="black", highlightcolor="black")
     time_mon.insert(tk.END, self.time_availability[0])

     time_tue = tk.Entry(highlightthickness=2,bg ='#E7E7E7')
     time_tue.place(x=150, y=125)
     #time_tue.config(highlightbackground="black", highlightcolor="black")
     time_tue.insert(tk.END, self.time_availability[1])

     time_wed = tk.Entry(highlightthickness=2,bg ='#E7E7E7')
     time_wed.place(x=150, y=175)
     #time_wed.config(highlightbackground="black", highlightcolor="black")
     time_wed.insert(tk.END, self.time_availability[2])

     time_thu = tk.Entry(highlightthickness=2,bg ='#E7E7E7')
     time_thu.place(x=150, y=225)
     #time_thu.config(highlightbackground="black", highlightcolor="black")
     time_thu.insert(tk.END, self.time_availability[3])

     time_fri = tk.Entry(highlightthickness=2,bg ='#E7E7E7')
     time_fri.place(x=150, y=275)
     #time_fri.config(highlightbackground="black", highlightcolor="black")
     time_fri.insert(tk.END, self.time_availability[4])

     time_sat = tk.Entry(highlightthickness=2,bg ='#E7E7E7')
     time_sat.place(x=150, y=325)
     #time_sat.config(highlightbackground="black", highlightcolor="black")
     time_sat.insert(tk.END, self.time_availability[5])

     time_sun = tk.Entry(highlightthickness=2,bg ='#E7E7E7')
     time_sun.place(x=150, y=375)
     #time_sun.config(highlightbackground="black", highlightcolor="black")
     time_sun.insert(tk.END, self.time_availability[6])

     return [time_mon, time_tue, time_wed, time_thu, time_fri, time_sat, time_sun]


if __name__ == '__main__':
  scrapper = TimeScrapper(["0","0","0","0","0","0","0",])
  print(scrapper.get_time())