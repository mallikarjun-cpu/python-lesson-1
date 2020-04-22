import math

def sqr_root (x):
    a = math.sqrt(x)
    return(a)

b = int(input("Enter a number: "))

#call the funtion and store in "res"
res = sqr_root(b)
print("Square root of",b,"is",res)
