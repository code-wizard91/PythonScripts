__author__ = 'Mizan'



list = ['suleman','hannah','foyez','mizan'] #here is a list, similar to an array

list[1] += 'wazaaaa' #+= can be used instead of list[1] = list[1] + 'wazaaa' for reassigning value

print(list[1])

l_1 = [1,2,3]       #these are all lists that will be used below in a matrix table
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1,l_2,l_3]  #here is a list matrix which contains all the lists created above

print(matrix[2][2]) # this will print the last element from the last list 9

#this is a dictionary where values are assigned to keys, use {} for dictionaries not []
my_dict = {'key1':'value1','key2':'value2'}


print(my_dict['key1']) #here is how you reference a value using a key

my_dict['key2'] += 'wawaw' #here is how you append to a value using +=

print(my_dict['key2'])

#use += to re assign values to lists and dictionaries

d = {} #here is an empty dictionary

d['name'] = 'mizan' #here is how you create new key and give it a value (key is name, value is mizan)
d['age'] = 23

print(d['name']) #same method to reference dictionary
print(d['age'])

#below is a dictionary(f_dict)containing 2 keys that have nested dictionaries in them : corporate and general
f_dict = {'corporate':{'mizan': 100,'john':200,'gary':300,'hanity':'423543'},'general':{'seema':'38722', 'shah':'32123121'}}

database_dict = {'usernames':{'Mizan':'guess123','katy':'orange123'}}

print(database_dict['usernames']['Mizan'][::-1])
print(f_dict['general']['seema'])


print(f_dict.keys())
print(f_dict['corporate'])

#dictionaries are unordered mappings
#they are different from sequences because they have no order and values are referenced using keyys
#dictionaries use curly braces not brackets like sequences