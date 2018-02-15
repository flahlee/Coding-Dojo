#find and replace
words = "It's thanksgiving day. It's my birthday, too!"
day = 'day'
print words.find(day)
print words.replace(day, "month")

#min and max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#first and last
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
newX= [x[0],x[7]]
print newX

#new list
'''sort list first- split list in half- 
push the list created from the first half to position O of the list created from the second half'''

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_half= x[len(x)/2]
second_half= x[len(x)/2:]
print first_half
print second_half
