import sys
#we will add stdin in a list
inputlist = []
phonebook = {}
for line in sys.stdin:
	inputlist.append(line)
#slice the list
n = int(inputlist[0])
entries = inputlist[1:n+1]
queries = inputlist[n+1:]	
#update the phone books
for entry in entries:
	name, phone = entries.split()
	phonebook[name] = phone

for query in queries:
	strippedquery = query.rstrip()
	if strippedquery in phonebook:
		print(strippedquery + "=" + str(phonebook[strippedquery]))
	else:
		print("not found")