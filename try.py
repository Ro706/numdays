print ("Enter date,month,than year")
d=int(input("enter date: "))
m=int(input("enter month: "))
y=int(input("enter year: "))
print (d,"/",m,"/",y)

def leapornot(y):
    n=0
    if y%100==0:
        if y%400==0:
            n=29
        else:
            n=28
    elif y%4==0:
        n=29
    else:
        n=28
    l=n-d
    print(l)
def month(m):
    if m==1:
        x = 31
        l=x-d
        print (l)
    elif m==2:
        leapornot(y)
    elif m==3:
        x = 31
        l=x-d
        print (l)
    elif m==4:
        x = 30
        l=x-d
        print (l)
    elif m==5:
        x = 31
        l=x-d
        print (l)
    elif m==6:
        x = 30
        l=x-d
        print (l)
    elif m==7:
        x = 31
        l=x-d
        print (l)
    elif m==8:
        x = 31
        l=x-d
        print (l)
    elif m==9:
        x = 30
        l=x-d
        print (l)
    elif m==10:
        x = 31
        l=x-d
        print (l)
    elif m==11:
        x = 30
        l=x-d
        print (l)
    elif m==12:
        x = 31
        l=x-d
        print (l)

print ("number of day left in this month are: ")
month(m)
