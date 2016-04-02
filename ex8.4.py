# # opne a file 
# fhandle = open("romeo.txt")
# read = fhandle.read()
# lst = list()
# for line in read:
# 	word = read.split()
# 	for words in word:
# 		if words not in lst:
# 			lst.append(words)
# lst.sort()
# print lst

# def sort_by_length(words):
# 	lst = list()
# 	for word in words:
# 		lst.append((len(word),word))
# 	# The keyword argument reverse=True 
# 	# tells sort to go in
# 	# decreasing order. 
# 	lst.sort(reverse=True) 

# 	res = list()
# 	for length,word in lst:
# 		res.append(word)
# 	return res 
# a = sort_by_length("There is") 
# print a


# import string

# fhandle = open('romeo.txt')
# counts = dict()
# for line in fhandle:
# 	line = line.translate(None,string.punctuation)
# 	line = line.lower()
# 	words = line.split()
# 	for word in words:
# 		if word not in counts:
# 			counts[word] = 1
# 		else:
# 			counts[word] += 1

# lst = list()

# for key,val in counts.items():
# 	lst.append((val,key))

# lst.sort(reverse = True)

# for key,val in lst [:10]:
# 	print key,val



# name = raw_input("Enter file:")
# if len(name) < 1: name = "mbox-short.txt"

# try:
# 	fhandle = open("mbox-short.txt")
# except:
# 	print 'Cannot open file: ',file,'.','Please Try again'
# 	exit()

# counts = dict()


# for line in fhandle:
# 	if not line.startswith('From '): continue
# 	word = line.split(':')
# 	# print word
# 	words = word [1]
# 	# print words
# 	counts[words] = counts.get(words,0)+1
# 	# print counts
# 	t = counts.items()
# lst = list()
# for key,val in t:
# 	lst.append((val,key))
# lst.sort(reverse=True)
# for val,key in lst[:30]:
# 	print key,val
# print t
# a = sorted(t)
# # print a
# for k,v in sorted(t):
# 	print k,v

# print counts.items()
# for (k,v) in counts.items():
# 	lst.append((v,k)) 
# lst.sort(reverse=True)
# v,k = lst[0]
# print k,v

		




# lst = list()
# for key,val in counts.items():	
# 	lst.append((val,key))
# lst.sort(reverse=True)
# val,key = lst[0]
# print key,val

# handle = open("mbox-short.txt")

# count = dict()

# for line in handle:
#     if not line.startswith("From "): continue
#     words = line.split()
#     word = words[1]
#     #print word
#     count[word] = count.get(word,0)+1
# # print count.items()

# bigCount = None
# bigWord = None

# for word,count in count.items():
# 	if bigCount is None or count > bigCount:
# 		bigCount = count 
# 		bigWord = word

# print bigWord,bigCount
			



fhand = open ('mbox-short.txt')
counts =dict()
for line in fhand:
	if not line.startswith('From '): continue
	words = line.split()
	for word in words:
		counts[word]=counts.get(word,0)+1
# print counts.items()

lst = list()
for key,val in counts.items():
	newtup = (val,key)
	lst.append(newtup)
lst.sort(reverse=True)

for key,val in lst:
	print key,val

