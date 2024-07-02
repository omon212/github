# import os
# from random import randint
#
# for i in range(1):
#     for j in range(0, randint(1, 10)):
#         d = str(i) + ' days ago'
#         with open('file.txt', 'a') as file:
#             file.write(d + '\n')
#         os.system('git add .')
#         os.system('git commit --date="' + d + '" -m "hello"')
#
# os.system('git push -u origin main')


import datetime
import time
import pytz

# Define the Uzbekistan time zone
uzbekistan_tz = pytz.timezone('Asia/Tashkent')

while True:
    now = datetime.datetime.now(uzbekistan_tz)
    if now.hour == 23 and now.minute == 41:
        print_hello_world()
        time.sleep(60)
    else:
        time.sleep(30)


