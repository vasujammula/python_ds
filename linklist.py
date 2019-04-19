class node:
	def __init__(self,v):
		self.value=v
		self.next=None

class linklist:
	def __init__(self):
		self.head=None
	def add(self,v):
		n=node(v)
		n.next=self.head
		self.head=n
		self.show()
	def show(self):
		c_node=self.head
		while(True):
			if c_node==None:
				print("Nothing to Display!!!")
				break
			elif c_node.next!=None:
				print("Current Node is :",c_node.value)
				c_node=c_node.next
			else:
				print("Current Node is :",c_node.value)
				break
	def rem(self,v):
		p_node=self.head
		while(True):
			if p_node.next==None:
				#only one node scenario  
				if p_node.value==v:
					print("Deleting the Node :",p_node.value)
					self.head=None
					self.show()
					break
				else:
					print("Element Not found in link list")
					self.show()
					break
			else:
				#more than one node present 
				n_node=p_node.next
				if p_node.value==v:
					print("Deleting node:",p_node.value)
					self.head=p_node.next
					self.show()
					break
				else:
					if n_node.value==v:
						p_node.next=n_node.next
						print("Deleting Node :",n_node.value)
						self.show()
						break
					else:
						p_node=p_node.next
						
						
			
