class node:
	def __init__(self,value,next=None):
		self.value=value
		self.next=next
class linklist:
	def __init__(self):
		self.head=None
	def add(self):
		v=input("Enter value of Node")
		n=node(v)
		n.next=self.head
		self.head=n
	def size(self):
		c=0
		c_node=self.head
		while(True):
			if c_node==None:
				print("No nodes in list so far")
				break
			elif c_node.next==None:
				c=c+1
				break	
			else:
				c=c+1
				c_node=c_node.next
		print("No of Nodes!!!:"+str(c))
	def display(self):
		c_node=self.head
		while(True):
			if c_node==None:
				print("Nothing to Display!!!!")
				break
			else:
				print("This is one of the value")
				print(c_node.value)
				if c_node.next==None:
					break
				else:
					c_node=c_node.next
	def delete(self):
		print("Enter Node to delete")
		v=input()
		p_node=self.head		
		while(True):
			if p_node==None:
				print("Noting to delete")
				break
			elif p_node.next!=None:
				c_node=p_node.next
				if p_node.value==v:
					print("Deleting ...",p_node.value)
					self.head=c_node
					break
				elif c_node.value==v:
					print("Deleting ...",c_node.value)
					p_node.next=c_node.next
					break
				elif p_node.next!=None:
					p_node=p_node.next
			else:
				print("Deleted: ",p_node.value)
				self.head=None
				break
