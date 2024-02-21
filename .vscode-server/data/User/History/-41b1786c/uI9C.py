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
