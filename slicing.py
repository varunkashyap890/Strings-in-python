# string in python can be sliced  for getting a part of the string

# name = 'INDIA'

name='AUSTRALIA'
# print(name)

# print(name[0:3])
# print(name[0:9:2])
# print(name[:])

# print(name[-4:])
# print(name[:-1])

print(len(name))   # len--> function is used to calculate length of string 

print(name.endswith("LIA"))  # str.endswith("LIA") ends with gives output--> True or False

print(name.count('A'))    # str.count('A')  --> counts number of A in the given string

country="india"
print(country.capitalize())  # str.capitalize() --> Capitalize the first Alphabet of String

print(country.find('d'))  # str.find('d') --> return the index of Alphabet

word='find'
print(word.replace('f','k'))