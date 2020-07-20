def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "azertyuiopmlkjhgfdsqwxcvbn"
    sentence.replace(" ","")
    result = True
    for i in alphabet:
    	if i not in sentence:
    		result = False
    return result		
