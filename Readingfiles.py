

s = 'hello world'

mizans_contacts = {'anwar':'24663434','shah':'344321'}

print(s[::-1]) 


placeholder = 'String234'

print('Place my variable here: %s' %(placeholder))

print('Floating point number: %1.5f' %(15.145))

print('First variable {x} second: {y}'.format(x='mizan', y='hello'))

print('Hello student {g} Hope you had good holiday here is your result {d}'.format(g='Yahya',d='A*'))


my_list = [1,'mizan',3]

names = ['mizan','happy','john','kane']

print(names + ['doggy'])

file_obj = open('filler.txt','r+') #this file object is used to open filler.txt, we use the 'r' to tell the program that we are only reading from the file.

print(file_obj.read()) #this prints the contents of the file

file_obj.write(' hola esta la guaro \n im hacking this file to take youre moneyyy') #this writes to the file

for line in open('test.txt'):
    print(line)

file_obj.close()