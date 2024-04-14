print(' "Welcome to the driving test" ')
a = input("What is your name : ")
print("Good morning", a)
print("What is your age : ")
age = int(input())

if age < 18:
    print("You can't drive")
elif age==18:
    print("you can but stay safe")

elif age > 100:
    print("No joking")

else:
    print("You can Drive :)")