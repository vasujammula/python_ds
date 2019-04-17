l=[1,2,3,4,5,6,7,8,9]
def search(l,i):
	if l[len(l)//2]==i:
		print("Found!!!!")
	elif i<l[len(l)//2] and len(l)>1:
		print(l[:len(l)//2],i)
		search(l[:len(l)//2],i)
	elif i>l[len(l)//2] and len(l)>1:
		print(l[len(l)//2:],i)
		search(l[len(l)//2:],i)
	else:
		print("Not Found")
		
	
search(l,2)
search(l,3)
search(l,4)
search(l,5)
search(l,6)
search(l,7)
search(l,8)
search(l,11)
search(l,12)
search(l,13)
