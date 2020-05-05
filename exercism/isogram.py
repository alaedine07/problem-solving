def is_isogram(string):
    if len(string) == 0:
       return True
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sentence = string.lower()   
    result = True
    for char in sentence:
        if char in alphabet: 
            if sentence.count(char) != 1:
                result = False
    return  result
