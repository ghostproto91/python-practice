#gcd of two numbers

def hcf(a,b):
    least= a if (a<b) else b
    for i in range(1,least+1):
        if ((a%i==0) and (b%i==0)):
            gcd=i
    return gcd

x=int(input('Enter a positive integer: '))
y=int(input('Enter another positive integer: '))
print(f"The greatest common divisor of {x} and {y} is {hcf(x,y)}")
