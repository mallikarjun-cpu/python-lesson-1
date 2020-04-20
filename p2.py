somenum = [1,2,4,6,11,20]

i = 0

while i < 6:
    x = somenum[i] * somenum[i]
    i = i + 1
    print ("square of " , somenum[i - 1] , "is" , x)
