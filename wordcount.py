# 1 open file in python

def word_count(filename):
	poem_words = {}
	poem_text = open(filename)
	for line in poem_text:
		line = line.rstrip()
		words = line.split(" ")
		
# 2 word count - space separated words
		for word in words:
			# if word in poem_words:
			# 	poem_words[word] = poem_words[word] + 1
			# elif word not in poem_words:
			# 	poem_words[word] = 1
			temp_value = poem_words.get(word, 0) # tell me what temp_value is
			poem_words[word] = temp_value + 1 # adds a value
	# print poem_words

# 3 print word count - .items() or .iteritems()
	for key, value in poem_words.iteritems():
		print "{} : {}".format (key, value)

word_count("twain.txt")
