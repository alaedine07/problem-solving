def is_valid(isbn):
	isbn = isbn.replace("-","")
	if len(isbn) != 10:
		return False
	res = isbn.isdigit()
	if res == 'False':
		return False
	sum = 0
	x=10
	for i in isbn:
		if i.isnumeric():
			sum = sum + (int(i)*x)
			x = x - 1
	if ((sum % 11 == 0)):
		return True		
