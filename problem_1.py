#!/usr/bin/python3

import datetime

today=str(datetime.date.today())
current_year=int(today[:4])
name=input("Hey, what is your name :")
age=int(input("Tell me your age and i'll show you some magic :"))
x=95-age
y=current_year+x
print(name, "you will be 95 years old in ",y)

