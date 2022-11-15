#cs practical
#sum of the series:1+x+x^2+x^3+.......
x=int(input("The value of x:"))
n=int(input("Highest power of series:"))
series=0
for i in range (n+1):
    y=x**i
    series=series+y
print (series)