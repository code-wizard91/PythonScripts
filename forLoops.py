myList = [1,2,3,4,5]

for i in myList: #this is the syntax for a for loop in python
    if(i%2==0): #modulo is used here to find even numbers in the list. any number that returns zero when using % is even
        print('number is even')
        print(i)



list = [1,2,3,4,5]



tupleList= [(2,3),(5,6),(4,6)] #tuples are immutable and cannot be changed.

for t1,t2 in tupleList:
    print(t1,t2)

kDict = {"k1":1,"k2":2,"k3":3}

for a,b in kDict.items():
    print(a,b)


myDict={'Id1':32432,'Id2':32432,'Id3':32432,'Id4':32432,'Id5':32432,'Id6':32432,'Id7':32432,'Id8':32432,}

for key,value in myDict.items(): # the .items() lets us access each element and key in the dictionary.
    print(key,value)

