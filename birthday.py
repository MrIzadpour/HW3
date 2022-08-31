from datetime import datetime

now = datetime.now()
date_string = now.strftime("%d/%m/%Y %H:%M:%S")
current_year = int(date_string[6:10])
current_month = int(date_string[3:5])
current_day = int(date_string[0:2])
current_hour = int(date_string[11:13])
current_minutes = int(date_string[14:16])
current_seconds = int(date_string[17:])


class BirthDay:
    year: int
    month: int
    day: int
    hour: int

    def age_to_year(self):

        #   determine year and month
        if current_month > self.month:
            m = abs(current_month - self.month)
            y = abs(current_year - self.year)
            m_hour = (abs(current_month - self.month)) * 30 * 24
            y_hour = (current_year - self.year) * 365 * 24
        elif current_month < self.month:
            m = abs((self.month - 12) + current_month)
            y = abs(current_year - self.year) - 1
            m_hour = (abs(self.month - 12) + current_month) * 30 * 24
            y_hour = ((current_year - self.year) - 1) * 365 * 24
        else:
            m = 0
            y = current_year - self.year
            m_hour = 0
            y_hour = (current_year - self.year) * 365 * 24

        #   determine day
        if current_day > self.day:
            d = current_day - self.day
            d_hour = (current_day - self.day) * 24
        elif current_day < self.day:
            d = (abs(self.day - 30) + current_day) + 1
            d_hour = ((abs(self.day - 30) + current_day) + 1) * 24
        else:
            d = 0
            d_hour = 0
            m = current_minutes

        print(f"you are {y}  ,{m} month and {d} years old ")
        h = abs(current_hour - self.hour)
        mi = current_minutes
        sec = current_seconds
        calc = y_hour + m_hour + d_hour + h
        print(f'your are {calc} hours and {mi} minutes and {sec} seconds')

    def times_left_BD(self):
        if current_month > self.month:
            m = (12 - current_month) + self.month
        elif current_month < self.month:
            m = abs(current_month - self.month)
        else:
            m = 0

        # determine left days
        if current_day > self.day:
            d = abs(current_day - self.day)
        elif current_day < self.day:
            d = abs((30 - self.day) + current_day)
        else:
            d = 0

        if m == 0 and d > 1:
            m = 12
        if m == 0 and d == 0:
            print('your birthday is today')
        else:
            print(f'your birthday is in {m} month and {d} days')


birth_day = BirthDay()
y_input = int(input('enter year of your birth: '))
m_input = int(input('enter month of your birth: '))
d_input = int(input('enter day of your birthday: '))
h_input = int(input('enter hour of your birth: '))
birth_day.year = y_input
birth_day.month = m_input
birth_day.day = d_input
birth_day.hour = h_input

birth_day.age_to_year()
birth_day.times_left_BD()
