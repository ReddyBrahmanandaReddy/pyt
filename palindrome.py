n=int(input(""))
temp=n
rem=0
while(n>0):
	a=n%10
	rem=rem*10+a
	n=n//10
if(temp==rem):	
     print("yes",end="")
else:
     print("no",end="")
