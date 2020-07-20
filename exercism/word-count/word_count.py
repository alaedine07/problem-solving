def count_words(sentence):
    
	sentence = sentence.lower().replace(',', ' ').replace('_', ' ').replace('\n', ' ').replace('\t', ' ').split(' ')
	wordlist = {}
	for word in sentence:
		word = word.strip(" .'\' !:,'\"@$%^&")
		if word != '':
			if word not in wordlist:
				wordlist.update({word: 1})
			else:
				wordlist[word] += 1	
	return wordlist

