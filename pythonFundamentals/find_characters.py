'''input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world'] '''

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
for item in word_list:
	if char in item:
		print item
		
