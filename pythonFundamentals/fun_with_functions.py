#Odd/Even:
for item in range(1,20001):
	if item % 2 != 0:
		print "Number is", item, "This is an odd number."
	else:
		print "Number is", item, "This is an even number."

#Multiply:
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr 
a = [2,4,10,16]
b = multiply(a,5)
print b 



#Hacker Challenge
def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
