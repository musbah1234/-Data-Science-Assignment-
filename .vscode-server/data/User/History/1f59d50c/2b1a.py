# Create an empty tuple
tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

bros_tup = ('ali', 'yusheu', 'sanusi', ' yau', 'magagi')
sis_tup = ('hafsa', 'naima', 'kadija', 'bintu')

# Join brothers and sisters tuples and assign it to siblings

siblings_tup = bros_tup + sis_tup

# How many siblings do you have?

print(len(siblings_tup))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

f_m = ('muktar', 'hajara')

family_members = siblings_tup + f_m

print(family_members)

# Unpack siblings and parents from family_members

a, *rest = family_members

print(family_members)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruit_t = ('mango', ' cashew', 'banana')

veg_t = ('lettuce', ' onions', 'carrot')

animal_t = ('fish', 'cow', 'chiken') 

food_stuff_tp = fruit_t + veg_t + animal_t

print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt  = list(food_stuff_tp)

print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle_items = food_stuff_lt[len(food_stuff_lt)//2-1:len(food_stuff_lt)//2+1]

