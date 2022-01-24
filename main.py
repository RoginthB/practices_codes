n=int(input("enter the number : "))
a=0
b=0
sum=0
for i in range(1,n+1):
    for j in range(i):
        a+=2
        if i==1:
            b=3
        else:
            b+=4
        sum=a*b
        print("%.5d"%(sum),end=" ")
    print( )
