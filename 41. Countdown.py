import datetime, bday_messages
bday_messages.path.append("C:\Users\shrey\OneDrive\Documents\Codedex\bday_messages.py")


today = datetime.date.today()

next_birthday = datetime.date(2025, 12, 8)

time_difference = today - next_birthday

days_away = next_birthday - today

if today == next_birthday:
    print(messages)

else:
    print('My next birthday is ' + str(days_away) + ' days away!')

