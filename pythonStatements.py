__author__ = 'Mizan'

#Will be exploring differences in statements in python compared to other languages

# if statements in most other languages would look like this
# ** if(a>b){
#   a=2;
#   b=4;
# }

a = 5
b = 3

if a<b:             #in python we do not use semi colons to denote the end of a statement, the end of a line is the end of the statement
    a = 5;
    print(a)
elif a>b:
    print('A is larger than b')
else:
    print('error')

