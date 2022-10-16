from datetime import datetime, timedelta
from datetime import date
import pandas

class Schedule:
    filename = "schedule.csv"
    today = ""
    weekly_availability = []
    time_availability = {}
    daily_hours = []
    existing_schedule = {}

    def __init__(self, time_av, dh):
        self.weekly_availability = time_av
        self.daily_hours = dh

        self.today = date.today()
        self.today = self.today.strftime("%m/%d/%y")

        self.get_previous_schedule()

    def get_previous_schedule(self):
        cur_schedule = self.get_schedule()
        if not (cur_schedule is pandas.DataFrame.empty):
            for i in cur_schedule.index:
                day = cur_schedule.at[i, "Date"]
                time = cur_schedule.at[i, "Time"]
                time = time[-8:]

                week_day = datetime.strptime(day, "%m/%d/%y").date().weekday()
                hours = cur_schedule.at[i, "Hours"]

                self.existing_schedule[day] = self.daily_hours[week_day] - hours
                self.time_availability[day] = time

    def update_time_availability(self, last_day):
        current_day = date.today()
        while current_day != last_day:
            day = current_day.strftime("%m/%d/%y")
            week_day = current_day.weekday()
            self.time_availability[day] = self.time_availability.get(day, self.weekly_availability[week_day])
            print(day, self.time_availability[day])

            current_day = current_day + timedelta(1)

    def get_schedule(self):
        try:
            current_av = pandas.read_csv(self.filename)
            return current_av
        except:
            return pandas.DataFrame.empty

    def add_due_date(self, due_date, course, hours):
        current_day = datetime.strptime(due_date, "%m/%d/%y").date()
        self.update_time_availability(current_day)

        current_day = current_day - timedelta(1)
        schedule = self.create_schedule(hours, current_day)
        dates, times, hours, subject = [], [], [], []

        for key in schedule:
            dates.append(key)
            subject.append(course)
            times.append(self.to_time_interval(self.time_availability[key], schedule[key]))
            hours.append(int(schedule[key]))

        f = open(self.filename, 'a+')
        f.close()

        df = pandas.DataFrame({"Date" : dates, "Time": times, "Hours": hours, "Course": subject})
        df.to_csv(self.filename, index=False)

    def create_schedule(self, hours, current_day):
        days_left = (current_day - date.today()).days

        avg_study = max(1, round(hours / days_left, 2))
        schedule = {}
        
        self.assign_time_to_date(current_day + timedelta(1))

        while hours > 0 and days_left > 0:
            date_formatted = current_day.strftime("%m/%d/%y")

            if self.existing_schedule[date_formatted] >= avg_study:
                date_formatted = current_day.strftime("%m/%d/%y")
                schedule[date_formatted] = schedule.get(date_formatted, 0) + min(avg_study, hours)

                self.existing_schedule[date_formatted] -= min(avg_study, hours)
                hours -= avg_study

            days_left -= 1
            current_day = current_day - timedelta(1)

        return schedule

    def assign_time_to_date(self, last_day):
        current_day = datetime.today().date() + timedelta(1)
        while current_day != last_day:
            date_formatted = current_day.strftime("%m/%d/%y")
            week_day = current_day.weekday()
            self.existing_schedule[date_formatted] = self.daily_hours[week_day] - self.existing_schedule.get(date_formatted, 0)

            current_day = current_day + timedelta(1)

    def to_time_interval(self, time_interval, hours_of_study):
        start_time = datetime.strptime(time_interval[0:5], "%H:%M").time()
        delta = timedelta(hours=hours_of_study)

        end_time = (datetime.combine(date(1, 1, 1), start_time) + delta).time()
        return f'{start_time} to {end_time}'


if __name__ == '__main__':
    temp = Schedule(['09:00-12:00', '13:00-15:00', '00:00', '16:00-21:00',
                         '09:00-11:00', '00:00', '09:00-21:00'],
                        [3, 2, 0, 5, 2, 0, 12])
    temp.add_due_date("10/21/22", "MATH 152", 5)

    scheduler = temp.get_schedule()
    print(scheduler)
    print(scheduler.index)
    print(scheduler.at[0, 'Hours'])