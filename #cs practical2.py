#sum of the series:x-(x^2)/2+(x^3)/3......

x=int(input("The value of x:"))
n=int(input("Highest power of series:"))
series=0
for i in range(1,n+1):
    y=((x**i)*((-1)**(i+1)))/i
    series=series+y
print (series)