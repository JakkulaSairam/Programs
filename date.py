"""difference between dates"""
from datetime import date
import datetime
l=list(map(int,input().split("-")))
h=list(map(int,input().split("-")))
isValidDate = True
try:
    datetime.datetime(l[2],l[1],l[0])
    datetime.datetime(h[2],h[1],h[0])

except ValueError :
        isValidDate = False
        if(isValidDate) :
            f_date = date(l[2],l[1],l[0])
            l_date = date(h[2],h[1],h[0])
            delta = l_date - f_date
            print(delta.days+1)
        else :
            print ("-1")