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
