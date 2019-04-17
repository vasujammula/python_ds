import sys
l=[3,1,5,9,2,8,4,7,6]
i=0
def find_min(t,ti):
	min=t[ti]
	min_pos=ti
	j=ti
	while(j<len(t)):
		if t[j]<min:
			min_pos=j
			min=t[j]
		j=j+1
	print("minimum from {l} is {m} and ti is {ti}".format(l=t,m=min,ti=ti))
	return min_pos	
while(i<len(l)):
	pos=find_min(l,i)
	print(" i is {i} and pos is {pos}".format(i=i,pos=pos))
	l[i],l[pos]=l[pos],l[i]
	print("List during the Iteration of :",i,l)
	i=i+1
print("Final List is :")
print(l)
