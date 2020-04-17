# quiz

#q1
print("which is the longest river in the world?")
ans1_list = ["1: kaveri","2: nile","3: amazon","4: ganga"]
print (ans1_list[0])
print (ans1_list[1])
print (ans1_list[2])
print (ans1_list[3])

x = int(input("type 1 ,2 ,3 or 4: "))

if x == 2 :
    print ("correct\n")
else :
    print ("wrong\n")
    
# q2
print("which is the largest country in the world?")
ans1_list = ["1: india","2: USA","3: russia","4: china"]
print (ans1_list[0])
print (ans1_list[1])
print (ans1_list[2])
print (ans1_list[3])

y = int(input("type 1 ,2 ,3 or 4: "))

if y == 3 :
    print ("correct\n")
elif y !=3:
    print ("wrong\n")

#q3
print("which is the biggest ocean in the world?")
ans1_list = ["1: pacific ocean","2: indian ocean","3: arctic ocean","4: atlantic ocean"]
print (ans1_list[0])
print (ans1_list[1])
print (ans1_list[2])
print (ans1_list[3])

z = int(input("type 1 ,2 ,3 or 4: "))

if z == 1 :
    print ("correct\n")
else :
    print ("wrong\n")

#decider
if (x == 2 and y == 3 and z == 1):
    print("YOU ARE A WINNER !!!")
else:
    print("please try again.")
