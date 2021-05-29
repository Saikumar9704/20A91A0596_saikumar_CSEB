n=int(input('enter number'))
i=1
print('factors of %d are:'%(n))
while i<=n:
	if n%i==0:
		print(i)
		i+=1
	else:
		i+=1
'''
output
enter number 64
factors of 64 are:
	1
	2
	4
	8
	16
	32
	64
	'''
© 2021 GitHub, Inc.
