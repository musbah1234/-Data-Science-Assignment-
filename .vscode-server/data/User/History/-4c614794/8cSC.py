# Find the length of the set it_companies

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

it_companies.add('twitter')

print(it_companies)


# Insert multiple IT companies at once to the set it_companies

new_it_companies = {"meta", "x", "intell"}

it_companies.update(new_it_companies)
print(it_companies)

# Remove one of the companies from the set it_companies

it_companies.discard('Amazon')

# Print the updated set
print(it_companies)
