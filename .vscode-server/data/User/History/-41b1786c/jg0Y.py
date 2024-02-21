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


# Go to the data folder and use the countries.py file. 
# Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
# Loop through the countries and extract all the countries containing the word 'land'
countries_with_land = [country for country in countries if 'land' in country.lower()]

# Print the result
print("Countries containing the word 'land':", countries_with_land)


