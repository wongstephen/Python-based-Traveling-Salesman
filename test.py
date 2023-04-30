import datetime

time_str = "11:32am"
try:
    time_obj = datetime.datetime.strptime(time_str, "%I:%M %p")
    print(time_obj)
except ValueError:
    print('broken')
