import datetime
date =datetime.datetime.now()
# will return current date with format
print(date.strftime("%d:%m:%Y"))


print(datetime.date.today().day)

# Keyword arguments — order doesn't matter
x=datetime.datetime(year = 2020,day = 2,month=12)
y=datetime.datetime(year =2020,day =5,month=11)
print(y-x)