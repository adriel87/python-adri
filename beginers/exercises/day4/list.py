# Day 04 List 30 days of python

# Declare an empty list

empty_list = []

# Declare a list with more than 5 items

more_than_five_list = [1,2,3,4,5,6]

# Find the length of your list

print(len(more_than_five_list))

# Get the first item, the middle item and the last item of the list
print(more_than_five_list[0], more_than_five_list[len(more_than_five_list)//2], more_than_five_list[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['adriel', 35, 1.72, True, 'calle la pasion']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'CCC'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('BitBox')

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Razer')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[-1] = it_companies[-1].upper()

# Join the it_companies with a string '#;  '
it_companies_list= '#;  '.join(it_companies)
print(it_companies_list)

# Check if a certain company exists in the it_companies list.
print('Exist MapySl in it_companies : ', 'MapySl' in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
first_3_it_companies = it_companies[0:3]
print(first_3_it_companies)

# Slice out the last 3 companies from the list
last_3_it_companies = it_companies[-3:]
print(last_3_it_companies)


# Slice out the middle IT company or companies from the list
middle_it_company = it_companies[ len(it_companies)//2 : len(it_companies)//2+1 ]
print(middle_it_company)

# Remove the first IT company from the list
firs_it_company = it_companies.pop(0)
print(firs_it_company)

# Remove the middle IT company or companies from the list
del it_companies[len(it_companies)//2 : len(it_companies)//2+1]
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# print(it_companies)

# Join the following lists:


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux.

full_stack.append('Python')
full_stack.append('SQL')

print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f'min {min_age} and max {max_age}')

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages[len(ages)//2])
# Find the average age (sum of all items divided by their number )
average = 0

for age in ages:
    average += age
average /= len(ages)

print(average)

# Find the range of the ages (max minus min)
print(max_age - min_age , ' range age')
# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_age-average), abs(max_age-average) , sep=' min compare max ')
# Find the middle country(ies) in the countries list
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

is_even = len(countries)%2 == 0
print(countries[len(countries)//2])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[0:len(countries)//2+1]
second_half = countries[len(countries)//2+1:]
print(first_half)
print(second_half)
#  Unpack the first three countries and the rest as scandic countries.
first, second, third, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']