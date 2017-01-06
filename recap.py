#import a module from sys library
from sys import argv

# how to use escape characters
print 'This escapes single quote in <You\'d>'
print 'This lets you add a forward slash \\'
print 'This adds a newline \n in the sentence'
print 'This adds a tab \t between \t words.'


# define a function to print entire contents of input file 'f
def readall(f):
	print f.read()

# define a function to start reading a file from a given line number onwards
def rewind(f, line_num):
	f.seek(line_num)

# define a function to read only a single line from given file 'f'
def print_a_line(f):
	print f.readline()


# unpack argv into respective variables
# script name will be first value and file name will be second value stored in argv as argv="read.py testfile"
script, fin = argv

# now script = recap.py & fin = testfile

# open the file for reading
f = open(fin)


print "print entire file:"
readall(f)

print "rewind to begining:"
rewind(f,0)

print "print first line:"
print_a_line(f)

# this will print next line
print "print another line:"
print_a_line(f)

print "rewind again but to line 3:"
rewind(f,2) # note index starts from 0, so to read line#3, we need to provide 2 as input


print "print 3rd line from input file:"
print_a_line(f)

## lets create function which can return some values back


# define a function to add 2 numbers & return the result
def add(a, b):
	return a+b

# define a function to subtract 2 numbers & return the result
def sub(a, b):
	return a-b

# define a function to multiply 2 numbers & return the result
def mul(a, b):
	return a*b

# define a function to div 2 numbers & return the result
def div(a, b):
	if (b!=0): # check if denominator is not 0
		return a/b
	else:
		return "NaN Error"


print "%d + %d = %d" %(4,5,add(4,5))

print "%d - %d = %d" %(30, 18, sub(30,18))

print "%d * %d = %d" %(20, 10, mul(20,10))

print "%d / %d = %r" %(10, 5, div(10,5))

print "%d / %d = %r" %(20, 0, div(20,0))

# or create a new variable and print/manipulate value later

add_v = add(10,5)
print "add_v = %d" %add_v

## add 10 more to it
add_v += 10
print "add_v + 10 = %d" %add_v



### some useful functions from libraries

# split a sentence into individual word tokens using single space as the delimiter
sentence = "This is a quick recap of Python language basics"
words = sentence.split(' ')
print "tokens = ", words

# sort a list of tokens
sort = sorted(words)
print "sorted list: ", sort

# get first value from a list
first = words.pop(0)
print "first value = ", first

# note once a value is popped from a list, all subsequent values moves up in the list as popped value is removed
print "remaining words in list:", words

# get last value from a list
last = words.pop(-1)
print "last value = ", last

print "was list changed?,yes see here = ", words


# get specific index value from a list
word = words.pop(3)
print "4th value = ", word

## conditionals

# if-elif-else 

a = int(raw_input("provide a number: ")) ## note raw_input returns string value, so we need to typecast it to integer
b = int(raw_input("provide another number: "))
print a
print b
if a > b:
	print "%d is greater than %d" %(a, b)
elif a == b:
	print "%d is equal to %d" %(a, b)
else:
	print "%d is lesser than %d" %(a, b)


##### Loops & Lists

## create a empty list
empty = []

# create list with 4 elements
four = ['a', 'b', 'c', 'd']

# create a list with mixed type of elements
mixed = ['a', 1, 'b', 0, 'c', 4.5 ]

## lets iterate through each of the element using a for-loop

# prints all elements in the list
for i in four:
	print "i = %r" %i

# print first 3 elements only 
for i in range(0,3):
	print "four[%d] = %r" %(i, four[i])


# print mixed element. use %r as we don't know type of value
for i in mixed:
	print "mixed has %r" %i
