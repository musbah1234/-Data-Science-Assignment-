# Iterate 0 to 10 using for loop, do the same using while loop.
# Iterate 0 to 10 using for loop
print("Iterating 0 to 10 using for loop:")
for i in range(11):
    print(i)

# Iterate 0 to 10 using while loop
print("\nIterating 0 to 10 using while loop:")
i = 0
while i <= 10:
    print(i)
    i += 1


# Iterate 10 to 0 using for loop, do the same using while loop
# Iterate 10 to 0 using for loop
print("Iterating 10 to 0 using for loop:")
for i in range(10, -1, -1):
    print(i)

# Iterate 10 to 0 using while loop
print("\nIterating 10 to 0 using while loop:")
i = 10
while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle
# Write a loop to print a triangle pattern
for i in range(1, 8):
    print("#" * i)


# Use nested loops to create the following
# Use nested loops to create the pattern
for _ in range(8):
    for _ in range(8):
        print("#", end=" ")
    print()

# Print the following pattern:
    # Print the following pattern: x x = x*x
for i in range(11):
    print(f"{i} x {i} = {i*i}")


# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
    

# Iterate through the list and print out the items
my_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in my_list:
    print(item)


# Use for loop to iterate from 0 to 100 and print only even numbers
# Use for loop to iterate from 0 to 100 and print only even numbers
for num in range(0, 101, 2):
    print(num)


# Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range(1, 101, 2):
    print(num)



# Use for loop to iterate from 0 to 100 and print the sum of all numbers
total_sum = 0
for num in range(101):
    total_sum += num

print("The sum of all numbers from 0 to 100 is:", total_sum)


# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds
sum_even = 0
sum_odd = 0

for num in range(101):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("Sum of all even numbers from 0 to 100:", sum_even)
print("Sum of all odd numbers from 0 to 100:", sum_odd)

