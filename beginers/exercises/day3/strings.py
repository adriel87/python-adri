# Strings 3 day of 30 days whit phyton

thirty = "Thirty"
days = 'Days'
of, python = 'Of', 'Python'

print(thirty, days, of, python, sep=' ')

coding = 'Coding ' 'For ' 'All'
print(coding)

company = coding

print(company)

print(len(company))

company = str.upper(company)
company = str.lower(company)

print(str.capitalize(coding))
print(str.title(coding))
print(str.swapcase(coding))

print(coding[0:6])

print(coding.replace('Coding', 'Python'))
split_coding = coding.split(' ')
print(split_coding)

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

split_companies = companies.split(',')
print(split_companies)

print(coding[0])
print(coding[-1])

print(coding[10])

sentece_to_acronim = 'Python For Everyone'
words_of_sentence = sentece_to_acronim.split(' ')

acronim =''

for word in words_of_sentence:
    acronim += word[0]

print(acronim)

print(coding.index('C'))
print(coding.index('F'))

print(str.rfind('Coding For All People', 'l'))

print(str.index('You cannot end a sentence with because because because is a conjunction', 'because'))
print(str.rindex('You cannot end a sentence with because because because is a conjunction', 'because'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

print(coding.startswith('Coding'))
print(coding.endswith('coding'))

print('   Coding For All      ')
print('   Coding For All      '.strip(' '))


# is identifier

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_libraries = ' '.join(libraries)
print(join_libraries)

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')





