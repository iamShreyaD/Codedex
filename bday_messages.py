import random
from random import choice


messages = [
'Hope you have a very Happy Birthday! 🎈',
'It\'s your special day – get out there and celebrate! 🎉',
'You were born and the world got better – everybody wins! 🥳',
'Have lots of fun on your special day! 🎂',
'Another year of you going around the sun! 🌞'
]

msg_variable = random.choice(messages)


Create a new file called main.py.

Import both the datetime module as well as bday_messages (the last file).


today: Today's date, using the datetime.date.today() method.
next_birthday: The date for your next birthday, using the year, month, and day arguments.
A really cool thing you can do with date objects is addition and subtraction!

time_difference = date1 - date2

Use date subtraction to calculate how many days away today is from next_birthday. Then, assign the result to a new variable called days_away.

Then, create a control flow statement:

If today is equal to next_birthday, print the random_message variable (imported from bday_messages).
Else, print 'My next birthday is {days_away} days away!'.
The output should look something like this:

My next birthday is 42 days away!

Bonus: Instead of using a date in the future, what if we tried to see how many days it's been since a past event, like the release date of your favorite movie or game, or the date you were born? What about how many years or months it's been?

Help