import os
import shutil
import time

a = "C:\Users\amrit\OneDrive\Desktop\Python2\PRO-C99"

b = os.path.exists(a)
print(b)

seconds = 208920
seconds_in_day = 60 * 60 * 24
days = seconds // seconds_in_day

def show_time(time):
        time = int(time)
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time
        if day != 0:
                return "%dD %dH %dM %dS" % (day, hour, minutes, seconds)
        elif day == 0 and hour != 0:
                return "%dH %dM %dS" % (hour, minutes, seconds)
        elif day == 0 and hour == 0 and minutes != 0:
                return "%dM %dS" % (minutes, seconds)
        else:
                return "%dS" % (seconds)

print(show_time(12345))