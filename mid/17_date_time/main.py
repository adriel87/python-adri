from datetime import time, datetime, timedelta, date

now = datetime.now()

day = now.day
month = now.month
year = now.year

hour = now.hour
min = now.minute

timestamp = now.timestamp()

formatted_cur = datetime.strftime(now,'%m/%d/%Y, %H:%M:%S')
print(formatted_cur)

date_string = '5 December, 2019'
date_string_formated = datetime.strptime(date_string, "%d %B, %Y")
print(date_string_formated)

# new_year = date(2023,12,31)
new_year = datetime(2023,12,31,23,59,59)
the_beggining = datetime(1970,1,1,0,0,1)

diff_ny_now = new_year - now
diff_now_b = now - the_beggining
print(diff_ny_now)
print(diff_now_b)
