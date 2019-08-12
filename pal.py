sn=int(input())
temp=sn
rev=0
while temp!=0:
	rev=(rev*10)+(temp%10)
	temp=temp//10
if sn==rev:
	print("yes")
else:
	print("no")
