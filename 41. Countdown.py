import datetime, sys

# to add folder path not file
sys.path.append(r"C:\Users\shrey\OneDrive\Documents\Codedex")

import bday_messages


today = datetime.date.today()

next_birthday = datetime.date(2025, 12, 8)

time_difference = today - next_birthday

days_away = next_birthday - today

if today == next_birthday:
    # access random_messages as it is variable of bday_messages.py
    print(bday_messages.random_message)

else:
    # add .days to extract just the number of days
    print('My next birthday is ' + str(days_away.days) + ' days away!')

