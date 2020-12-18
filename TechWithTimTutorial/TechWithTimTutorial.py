#----------------------------------------------------------------------------------------------------------------------------------------------------
##Complete python tutorial by Tech with Tim
##https://www.youtube.com/watch?v=sxTmJE4k0ho
#----------------------------------------------------------------------------------------------------------------------------------------------------
#Table of contents:
#- Tutorial  1: Variables and Data types
#- Tutorial  2: Basic Operators and inputs
#- Tutorial  3: Conditions
#- Tutorial  4: if/elif/else
#- Tutorial  5: Chained conditionals (and, or, not) & nested statements
#- Tutorial  6: For loops
#- Tutorial  7: While loops
#- Tutorial  8: Lists and tuples
#- Tutorial  9: Iteration by item
#- Tutorial 10: String methods
#- Tutorial 11: Slice operator
#- Tutorial 12: Functions
#- Tutorial 13: How to read a text file line by line
#- Tutorial 14: Writing to a text file
#- Tutorial 15: Using .count() and .find()
#- Tutorial 16: Introduction to modular programming (import (and write own) modules)
#- Tutorial 17: Optional parameters
#- Tutorial 18: Try and Except (error handling)
#- Tutorial 19: Global vs local variables
#- Tutorial 20: Classes & objects - Tutorial 1: What are classes?
#- Tutorial 21: Classes & objects - Tutorial 2: How can they be created?
#- Tutorial 22: Classes & objects - Tutorial 3: What is inheritance/how is it used?
#- Tutorial 23: Classes & objects - Tutorial 4: Overloading default python methods
#- Tutorial 24: 


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 1: Variables and data types
#----------------------------------------------------------------------------------------------------------------------------------------------------

##To comment a line a # symbol is placed in front of it
##To comment a whole block of code ctrl+k+c can be used. To uncomment it's ctrl+k+u

##There are different data types: int, float, string, bool, ... (as in c++)

##bool: True and False have to start with a capital letter, otherwise it's not the keyword, but just a variable name

##variable names can contain underscores, but no dashes and they can't start with a number

##strings can be written with single or double quotation marks. Variables can be printed with the print() function
#a='Tim wants to test the print function'
#b="and how about double quotation marks as used in Germany?"
#print(a)
#print(b)

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 2: Basic Operators and inputs
#----------------------------------------------------------------------------------------------------------------------------------------------------

##input and output
#print('Hello, what is your name?')
#name=input()                           #The input() operator can be used to prompt an input from the user, input is treated as string
#print('Hi',name)                       #Strings can be concatenated by using a comma (also acts as a space)
#print('Hi '+name)                      #or by using the + sign (which does not act as a space) (same output for this example)

##To calculate an exponent two * symbols have to be used
#a=5
#b=4
#c=a**b
#d=str(a)+'^'+str(b)                     #creating string '5^4' without any spaces to use as output
#print(d,'=',c)                          #comma and plus methods can't be mixed in one print statement, but string variable can be declared before

##If the / operator is used the result is automatically given as a floating point value. For integer division use double /
#e=5/4                                   #normal division, result 1.25
#print(e)
#f=5//4                                  #integer division, result 1, decimal points are simply cut, no rounding
#print(f)
#g=5%4                                   #modulo operator, result 1, remainder of division
#print(g)

##input prompts a string, conversion of string to int
#print('Type in a number')
#num1=input()
#print('Type in another number')
#num2=input()
#SUM=num1+num2                           #Here the two numbers as strings are added, 4 and 5 would result in 45
#Sum=int(num1)+int(num2)                 #Here the two numbers are converted to integers and then added, 4 and 5 would result in 9
#print(SUM)
#print(Sum)

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 3: Conditions
#----------------------------------------------------------------------------------------------------------------------------------------------------

##Conditional operators: <, >, ==, !=, same as in c++ - one = is the assignment operator
##Strings can be compared as well
#print('Tim'!='Joe')                      #returns True

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 4: if/elif/else  &  Tutorial 5 - Part 1: Chained conditionals (and,or,not)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#a=5
#b=4.5

#if a==b:                                             #if condition, no brackets needed, body is indented, no curly braces
#    print('Hurray!')
#elif not(a==b):
#    print('Yey!')

##and --> Both conditions have to be true
##or  --> One of the conditions has to be true
##not --> reverses the condition not(a==b) is equivalent to a!=b

#age=int(input('Your age: '))                               #If an argument is passed it is displayed, conversion from string to int can already be done

#if age>=14 and age<16:                                     #Initial if condition, in python 'and' is used, not &&
#    print('Hey, you can give consent to have sex')
#elif age==16 or age==17:                                   #If first if condition is not met, this one is checked, 'or' is used instead of ||
#    print('Hey, you\'re allowed to have a beer')           #\' can be used in strings to display an apostrophe without ending the string
#elif age>=18 and age<21:                                   #Several different conditions can be checked with this command
#    print("Hey, you're allowed to have strong booze")      #Another option is to use "" for the string and use the apostrophe as usual
#else:                                                      #If no previous condition was True this command is executed 
#    print('You are allowed to enter a Casino')

##Conditions are checked one after the other, as soon as one is True the rest of the conditions aren't checked

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 5 - Part 2: Nested statements
#----------------------------------------------------------------------------------------------------------------------------------------------------

#a=5
#b=3

##if, elif and else statements can be nested which means written in the body of one another

#if a<b:
#    if b%2==0:               #Could be written as if a<b and b%2==0
#        print('Option 1')
#    else:                    #Could be written as elif a<b and b%2!=0
#        print('Option 2')
#else:
#    if b==4:                 #Could be written as elif a>b and b==4
#        print('Option 3')
#    else:                    #Would also be else and represents als cases where a>b and b!=4
#        print('Option 4')

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 6: For loops
#----------------------------------------------------------------------------------------------------------------------------------------------------

#for x in range(0,10,1): #start, end+1, step;  step=1 is default if left out --> for x in range(0,10): also works
#    print(x)

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 7: While loops
#----------------------------------------------------------------------------------------------------------------------------------------------------

##syntax:
##while condition:
##   body
##usually the body contains a variable that is incremented or decremented until a condition is met

##small little calculator, Nesting used in an useful way, condition set to true for loop that is ended by break statement
#while True:
#    print('Options: ')
#    print('1:add')
#    print('2:subtract')
#    print('3:multiply')
#    print('4:divide')
#    print('5:exit')
#    option=int(input('>'))
#    if option==5:
#        break                             #The break statement immediately ends the loop
#    else:
#        print('Enter two numbers:')
#        a=int(input('a= '))
#        b=int(input('b= '))
#        if option==1:
#            print(a,'+',b,'=',a+b,'\n')
#        elif option==2:
#            print(a,'-',b,'=',a-b,'\n')
#        elif option==3:
#            print(a,'x',b,'=',a*b,'\n')
#        elif option==4:
#            print(a,'/',b,'=',a/b,'\n')
#        else:
#            print('That\'s not a valid option')

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 8: List's and tuples (01:05:53)
#----------------------------------------------------------------------------------------------------------------------------------------------------

##Lists in python can contain a certain number of items of different types
##items in the list are numbered from 0 upwards
##len(listName) gives the number of items of a list, also works for len(stringName)
##if an item is to be added to the end of the list the listname.append(item) method can be used
##if an item is to be changed it's easily done by using listName[itemIndice]=newValue
##a tuple is quite similar to a list but created with round brackets instead of square brackets, it's used for colours or coordinates, more later

#fruits=['apple',1,'apricot',5,'banana',1,'cherry',10,'pear',1,'pineapple',0.5,'plum',5] 
#print('A good fruit salad contains:\n')
#for x in range(0,len(fruits),2):
#    if fruits[x+1]>1:
#        a=fruits[x]+'s'
#        print(fruits[x+1],a,'\n')
#    else:
#        print(fruits[x+1],fruits[x],'\n')

#print('did I forget anything?')
#print('yes/no')
#option=input('>')
#counter=0
#if option=='yes':
#    fruit=input('Enter the name of the fruit: ')
#    fruits.append(fruit)
#    number=int(input('Enter the number of these fruits that have to be added: '))
#    fruits.append(number)
#    counter=1
#else:
#    print('ok, then!')

#if counter>0:
#    print('\nA good updated fruit salad contains:\n')
#    for x in range(0,len(fruits),2):
#        if fruits[x+1]>1:
#            a=fruits[x]+'s'
#            print(fruits[x+1],a,'\n')
#        else:
#            print(fruits[x+1],fruits[x],'\n')

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 9: Iteration by item (01:14:15)
#----------------------------------------------------------------------------------------------------------------------------------------------------

##Instead of using the range() command (iteration by index) it is also possible to iterate through a list by item without this command
##This method is useful if all list items have to be checked for certain conditions and their position in the list is not needed
#fruitsNumbers=['apple',1,'apricot',5,'banana',1,'cherry',10,'pear',1,'pineapple',0.5,'plum',5] 
#fruits=[]
#numbers=[]
#for fruit in fruitsNumbers:                            #automatically stops at the end of the list, no len(listname) needed
#    if type(fruit)==int or type(fruit)==float:
#        numbers.append(fruit)
#    else:
#        fruits.append(fruit)

#print(fruits,'\n')
#print(numbers,'\n')

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 10: String methods (01:20:13)
#----------------------------------------------------------------------------------------------------------------------------------------------------

## .strip(), len(), .lower(), .upper(), .split; len() has already been covered, returns length of string or number of items of list used as input
#
#text=input('Input something: \n')
#print(text.strip(),'\n')                         #Removes spaces at the beginning and end of the string
#print(text.lower(),'\n')                         #Converts all letters within the string to lower case letters
#print(text.upper(),'\n')                         #Converts all letters within the string to upper case letters
#print(text.split('.'))                           #Splits string into parts at delimiter (dot) and puts parts into list, default delimiter is space

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 11: Slice operator (01:26:38)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#As items within a list can be accessed items in strings (in this case the character at that position) can be accessed as well
#text='I want to test accessing characters within a string'
#print(text[0])                                            #prints I
#fruits=['apple','pear','banana','cherry','raspberry']
#print(fruits[0])                                          #prints apple
#print(fruits[0][0])                                       #prints a (could for instance be used to order items within a list by alphabetical order)

#print(text[0:6:1]) 
##This is the slice operator, Works same way as range and can be used to extract parts of a string into a new string
##The syntax is string[start(default 0):stop(default end of string):step(default 1)], 
##the stop is used with <, so to get a word at the beginning with six letters the start is zero, but the stop is not 5, but 6

##Can also be used to insert an item into a list (for the end of the list fruits.append() can be used
#fruits[2:2]='pineapple'                                   #works for single characters, but splits strings into individual characters
#print(fruits)
#fruits[2:2]=['pineapple']                                 #works for strings and inserts them as one item
#print(fruits)

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 12: Functions (01:33:40)
#----------------------------------------------------------------------------------------------------------------------------------------------------

##Functions are usually defined at the beginning of the code file before they are used or in a separate file that is loaded
##Syntax: def functionName(parameter1, parameter2, ...):
##   code block
##   return returnValue

#import math #Has to be imported to use the sqrt function

##A function doesn't have to have parameters. E.g. 
#def printSmth():
#   print('That\'s what I always want to print')
#printSmth()
##would also work

#def addTwo(x):
#    return x+2

#b=addTwo(5)
#print(b)

##usually functions are a bit more difficult and let the user repeat tasks without having to code them every time
##This is an example of a function that checks if a number is a prime
#def isPrime(x):
#    for i in range(2,int(math.sqrt(x)),1):
#        if x%i==0:
#            print(i)
#            return False
#    return True

#print(isPrime(1213))

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 13: How to read a text file line by line (01:42:09)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#file=open('fruits.txt','r')            #file is opened with a permission to read, w for write, if second argument is forgotten file is cleared!!!
#f=file.readlines()                     #reads file line by line into a list
#print(f[3])

##one way to get rid of the commas at and line breaks at the end of each line
#newList=[]
#for line in f:
#    if line[-1]=='\n':                 #line[-1] means last character of string line
#        newList.append(line[:-2])      #-2 because the line break (not shown) and comma have to be removed, means read to end minus last two characters
#    else:
#        newList.append(line[:-1])
#print(newList[3])

##easier way to get rid of the line breaks
#newList2=[]
#for line in f:
#    newList2.append(line.strip(',\n')) #.strip() removes not only the spaces, but also line breaks, if string is given as argument it is removed
#print(newList2[3])

#file.close()                           #file should always be closed after use

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 14: Writing to a text file (01:50:30)
#----------------------------------------------------------------------------------------------------------------------------------------------------

##uses newList2 from previous tutorial
#file=open('Test.txt','w') #if file does not exist it is created, if it exists it is cleared and filled according to the commands
#for line in newList2:     #list can't be given directly as argument to .write, thus a for loop is used to write line by line
#    file.write(line+'\n') #does not work with a comma, but works with the + sign, instead of \n a comma could be used to create a csv file

#file.close()

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 15: Using .count() and .find() (01:54:48)
#----------------------------------------------------------------------------------------------------------------------------------------------------

##.count() and .find() can be used on strings

##.find() can be used to find the index of a certain element within a list or a character within a string
##The output for stringName.find('character') is the index at which this character is found for the first time. If it's not in there the output is -1
##To find the index of the fourth occurence of the character stringName.find('character',4) can be used

#String='Hello there. My name is Tim.'
#print('First H: '+str(String.find('H'))+'\n')                  #Keep in mind that the + method can only be used to concatenate strings. int don't work
#print('First h: '+str(String.find('h'))+'\n')
#print('Second e: '+str(String.find('e',2))+'\n')
#LIST=['apple','orange','pear','pineapple','apple']
#print('Index of apple: '+str(LIST.index('apple',2))+'\n')      #The list equivalent to .find() is .index()

##.count() counts how many characters of a certain type can be found within a string

#print('There is/are : '+str(String.count('H'))+' H within the string. \n')
#print('There is/are : '+str(String.count('h'))+' h within the string. \n')
#print('There is/are : '+str(String.count('el'))+' el within the string. \n')       #also works for several characters
#print('There is/are : '+str(LIST.count('apple'))+' apples within the list. \n')    #The .count() method also works for lists

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 16: Introduction to modular programming (02:01:46)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#In python modules with functions and classes can be imported
#While not necessary it often makes sense to abbreviate a module name making the commands faster to type
#While some modules are built in, others aren't and have to be downloaded before

#It is also possible to create own modules:
#-create txt file with module name in folder with main python code.
#-copy the functions you want to use into the file and save it
#-make sure to include import commands that are needed for the functions to run in the file
#-change file ending from .txt to .py
#-import module in main code
#-use functions with moduleName.functionName()

#Example in tutorial 12 above --> math module containing the sqrt(function)
#Other examples of useful modules:
#pygame: for game development (Not a built in module)
#os:     for file paths (images can be included, etc.)
#pyplot: for creating plots as in Matlab

#import math #as m                      #syntax is: import moduleName (as abb.)
#import matplotlib.pyplot as plt
#import myModule as mM

#a=5
##print(m.sqrt(a))
#print(math.sqrt(a))
#print(math.degrees(math.pi))           #math.degrees(radian)=degrees
#print(math.radians(180)/math.pi)       #math.radians(degrees)=radians

#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
##plt.show()

#print(mM.isPrime(29))

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 17: Optional parameters (02:09:43)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#import math

##If a function has several parameters, some of them can be given a default value that is used if no other parameter is used as input
##default parameters are given in a certain order. If you want to change the second optional parameter, you also have to type in the first one
##non-optional parameters should always be placed before optional ones

##Centripetal force at the equator
#def FzEq(m,v,r=6371000):                        #Average earth radius is taken as default, which is too small for the equator, but a good approximation
#    return (m*(v**2)/r)

##Velocity at the equator
#def velEq(r=6371000):                           #Average earth radius is taken as default again
#    U=2*math.pi*r
#    d=24*60*60
#    return U/d

##Centripetal force on a person of 78 kg mass
#print(FzEq(78,velEq()))                         #Since there is no argument given to velEq the default is used, same for FzEq with only two arguments


#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 18: Try and except (Error handling) (02:15:36)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#If for instance an user input is requested and if of wrong type crashed the program the try and except method can be used
#Might be worthwhile to find out if it can be used recursively within a function
#def Function():
#    try:
#        something
#    except:
#        print(something)
#        Function()


#number=input('Please type in a number:\n')
#try:                             #Try this code of block
#    number1=int(number)
#    print('Number saved')
#except:                          #But if it returns an error message do this (e.g. no underscore in password)
#    print('That was not a number! :(')

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 19: Global vs local variables (02:20:28)
#----------------------------------------------------------------------------------------------------------------------------------------------------

##If a variable is declared within a function it is not defined for other functions but can only be accessed within the 
##function it is declared in
##If a variable is declared outside of a function or class it is called a global variable
##Since in python there is no main() function as in C++ usually all variables are defined as global variables unless they are in a function or class
##This means they wouldn't have to be passed to a function but could be accessed by name within the function body
##This is bad practice, since the function wouldn't work if copied to another program without the variable declaration
##All values that are needed within a function should either be passed to the function or calculated from passed values within the function 
##The value of a global variable can't be changed within a function body

#a=5
#b=4

#def DoSmth(x):
#    #global b        #This enables changing a variable value within a function (b=7 instead of b=4 printed outside of function)
#    print(a)        #This is bad practice, print(x) would be the much better option
#    b=7             #Also bad practice and creates a copy of b that is changed only within the function body
#    x=x+5
#    return x

#print(DoSmth(a))
#print(b)
#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 20: Classes & objects - Tutorial 1 - What is it? (02:29:16)
#----------------------------------------------------------------------------------------------------------------------------------------------------

##basically everything you declare in python is an object.
##Apart from that the classObject.method() syntax is similar as in C++

#x=5
#y='   string   '

#print(type(x)) #output is <class 'int'> which means that all the variable types in python are classes and the variables objects of the respective class 
#print(type(y)) #output is <class 'str'> 

#b=y.strip()    #the .strip() syntax should already tell us that y has to be an object and .strip() is one of the str classes' methods
#print(b)
#print(y.replace('s', 'S')) #Might prove useful

##if help(varType) shows the class and all its methods

#help(int)

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 21: Classes & objects - Tutorial 2 - How can it be created? (02:39:00)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#class Dog(object):                       #object keyword can also be left out, but doesn't hurt to use it, (means that class Dog inherits from class object)
#    def __init__(self):                  #This is the default constructor of the class, It is called automatically each time a Dog object is created
#        pass                             #pass is like leaving a function body blank
#    def speak(self):
#        #print(str(self)+'\n')           #gives the Ram address, but unfortunately not the name of the instance 
#        print('Arf, arf! Woof!\n') 

#class Tree(object):
#    def __init__(self, name):
#        self.name=name                   #In this class there is a member variable name that is initialized by the constructor
#    def sway(self):
#        print(self.name+': \nThe ', self.name ,' gently sways in the wind. The sun shines warmly. Birds chirp.\n')
#    def Add_col(self,colour):            #If a variable (attribute) is added it has to be done with a method. As long as it hasn't been added, 
#        self.colour=colour               #it obviously can't be called (error if tried)
#        print('The ',self.name,'\'s leaves are',self.colour, 'and rustle softly in the breeze.\n')

#Sissi=Dog()                              #This is the python way to create a class object/instance of class dog
#Sissi.speak()                            #Function method is called with . operator like in C++

#Willow=Tree('Willow')                    #When creating the object the name is given to the constructor as an argument                       
#Willow.sway()
#Willow.Add_col('bright green')

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 22: Classes & objects - Tutorial 3 - What is inheritance? (02:50:37)
#----------------------------------------------------------------------------------------------------------------------------------------------------

#If for a project an number of similar class objects are to be used it is sensible to write a quite general parent class with the 
#attributes and methods that all objects should have in common and then save work with typing by creating child classes 
#that inherit all variables and methods of the parent class.
#Then variables and methods can be added or modified to fit the respective child class's requirements
#Inheritance can also be used over several steps (e.g. livingThing, animal, mammal, rodent, mouse)

class Dog(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old. \n")
    def talk(self):
        print("Bark! \n")


#class Cat(object):                                         #Copying code from another class (Dog) and adding one variable is bad practice/a lot of work
#    def __init__(self, name, age, colour):                 #Instead inheritance can be used as shown below
#        self.name=name
#        self.age=age
#        self.colour=colour
#    def speak(self):
#        print("Hi I am", self.name, "and I am", self.age, "years old. \n")

class Cat(Dog):                                             #This initializes a new class Cat with Dog as parent class
    def __init__(self, name, age, colour):                  #This is the constructor of Cat with the new variable colour
        super().__init__(name, age)                         #Here the constructor body of the super class (parent, Dog) is called
        self.colour=colour                                  #Here the new variable colour is assigned within the constructor body
    def talk(self):                                         #The definition of a function of the parent class can be overwritten
        print("Meow! \n")

Sissi=Dog("Sissi",6)
Sissi.speak()
Sissi.talk()

Amar=Cat("Amar", 12, "Black")                               
Amar.speak()                                                #Since Dog had the member function speak, Cat has inherited it and can use it
Amar.talk()                                                 #Since the member function talk of Dog was overwritten, the output is different

#----------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------
#Tutorial 23: Classes & objects - Tutorial 4 - Overloading default python methods (03:03:14)
#----------------------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------------------------
