print "Hello World!"
x = "Hello Python"
print x
y = 42
print y
#commenting a single line
#we can even comment out code
#print "this will not print!"

print "read below for more on multi-line comments in python!" #this would execute
# This line and below would not execute
'''
Triple quotations allow us to comment across multiple lines as long as
the triple quoted comment is not the first thing in your file.
You can use double or single quotes!
'''
'''print "hello" '''

#define  function that says hello to the name provided
#this starts a new block
def say_hello(name):
	#these lies are indented therefore part of the function
	if name:
		print 'Hello', + name + 'from inside the function'
	else:
		print 'No name'
	#now we're unindented and have ended the previous block
print 'Outside of the function'

print "this is a sample string"

name = "Zen"
print "My name is", name
#instead of comma we can also use +, but + won't add space between string and value

lastName = "Adams"
print "My last name is" + lastName



#we can also use curl brackets {} and the string .format() - known as string interpolation
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)


#adding below function will print all uppercase letters
x = "Hello World"
print x.upper()
#output: "HELLO WORLD"

fruits= ['apple', 'banana', 'orange', 'strawberry']
veggies = ['lettuce', 'cucumber', 'carrots']
fruits_and_veggies = fruits + veggies
print fruits_and_veggies
salad = 3 * veggies
print salad

drawer = ['document', 'envelopes', 'pen']
#access the drawer with index of 0 to 2 and print value
print drawer[0] 
print drawer [1]
print drawer [2]


#<list>.append (<new_element>)
x = [1,2,3,4,5]
x.append(99)
print x
#output would be [1,2,3,4,5,99]

#the starting index and ending index should be separated by ":"
x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];


#Ien(sequence)- returns the number of items in a sequence
my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3


#conditional expression- if, if else, else
'''if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'You are seventeen.'
else:
  print 'You are so young!' '''


#for loop
for count in range(0, 5):
	print "looping - ", count

words = "Its thanksgiving day. Its my birthday, too!"
print words.find('day')
print words.replace('day', 'month')




















