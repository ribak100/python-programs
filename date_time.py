import datetime

#help(datetime.date)

pycreator = datetime.date(1956, 1, 31)

print(pycreator)
print(pycreator.month)
print(pycreator.year)


crazy_day= datetime.date(2000, 1, 1)
how_long= datetime.timedelta(200)
back_to_normal= crazy_day + how_long
print("The back to normal date :" ,back_to_normal)
print("The crazy day :", crazy_day)
print("the crazy day took ", how_long , "before getting back to normal")
message= "The guy that created python was born on {: %A, %B %d, %Y}. "
print(message.format(pycreator))

'''i can print all individual occurences, i.e date only, month only, time only, sec only and etc'''
my_wedding_date = datetime.date(2020, 10, 15)
my_wedding_time = datetime.time(12, 30, 15)
my_wedding_datetime = datetime.datetime(2020, 10, 15, 12, 30, 15)

print("My wedding day = ", my_wedding_date)
print("My wedding time = ", my_wedding_time)
print("My wedding date and time = ", my_wedding_datetime)

now_time = datetime.datetime.today()

print(now_time)

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)











