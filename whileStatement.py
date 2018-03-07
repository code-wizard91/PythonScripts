__author__ = 'Mizan'

#format for while loop is
# while test:
#   //code statement
# else:
#   //final statement

x = 0;

while x!=10:
    x+=1
    print(x)        #this while loop will keep going until x is equal to ten or the test stetement becomes true
else:
    print('failed')



y = 0

while y<10:
    print('y is currently',y)
    y += 1


#next we explore break continue and pass

#break, breaks out of a loop

#continue goes to the top of the closes enclosing loop

#pass does nothing at all

z = 0

while z<10:
    print('z is currently ',z)
    print('z is still less than 10, adding 1 to z')
    z += 1

    if z == 5:
        print('Alert Memmory usage high!')
    else:
        print('continueing')
        continue



#if a statement that is being evaluated by a while loop is always true, an infinite loop will occur
#always avoid this