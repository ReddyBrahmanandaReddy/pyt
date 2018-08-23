num=int(input())
for i in range(1,6):
	if i<5:
		k=' '
	else:k=''
	dig=i*num
	print(dig,end=k)
