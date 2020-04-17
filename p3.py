x = int(input("enter x:"))
y = int(input("enter y:"))
z = int(input("enter z:"))

print ("the largest numer between" , x , y ,"and",z ,"is")
if (x > (y and z)):
    print (x)
elif (y > (x and z)):
    print (y)
else:
    print (z)


