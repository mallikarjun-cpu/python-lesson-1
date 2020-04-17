time = int(input("Enter the time: "))

if time > 5 and time < 12:
    print("Hi,good morning!")
elif time >= 12 and time < 16:
    print("Hi, good afternoon!")
elif time >= 16 and time < 19:
    print("Hi, good evening!")
elif time >= 19 and time < 23:
    print("Hi, good night!")
    
