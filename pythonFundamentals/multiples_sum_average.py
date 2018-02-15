# multiples
#part1 - print all the odd numbers from 1 to 1000- use for loop and dont use list
for i in range (1, 1001):
	if (i % 2 ==1):
		print i

#part 2 - print all the multiples of 5 from 5 to 1,000,000
for i in range(5, 1000001):
	if(i % 5 ==0):
		print i


#sum list - print the sum of all values 
a = [1,2,5,10,255,3]
print sum(a)


#average list - print the average of the values in the list
a = [1,2,5,10,255,3]
print sum(a)/len(a)