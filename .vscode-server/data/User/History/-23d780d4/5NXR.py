# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 

age = int(input("Enter your Age:"))

if age >= 18:
    print("You are old enough to drive")
else:
    Below = age - 18
    print(f"You need {Below} more years to learn to drive")