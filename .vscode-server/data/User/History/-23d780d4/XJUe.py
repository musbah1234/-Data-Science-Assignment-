# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 

age = int(input("Enter your Age:"))

if age >= 18:
    print("You are old enough to drive")
else:
    Below = 18 - age
    print(f"You need {Below} more years to learn to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    
me = int(input("Enter your age:"))
you = int(input("Enter your age:"))

if me > you:
    age_diff = me - you
    if age_diff == 1:
        print("you are 1 year older than me")
    else:
         print(f"you are {age_diff} years older than me")
elif you > me:
    age_diff = you - me
    if age_diff == 1:
        print("I am 1 year older than you")
    else:
        print("i am {age-diff} years older than you")