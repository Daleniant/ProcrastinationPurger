import csv
import time_scrapper
import pandas

class Availability:
    filename = 'time_availability.csv'
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def read_file(self):
        try:
            current_av = pandas.read_csv(self.filename)
            return current_av
        except:
            current_av = pandas.DataFrame({'Day': self.days, 'Time': ['00:00', '00:00', '00:00', '00:00', '00:00', '00:00', '00:00']})
            return current_av

    def update_file(self, time_input):
        new_av = {'Day': self.days, "Time": time_input}

        f = open(self.filename, 'w+')
        f.close()

        df = pandas.DataFrame(new_av)
        df.to_csv(self.filename, index=False)

if __name__ == '__main__':
    avc = Availability()
