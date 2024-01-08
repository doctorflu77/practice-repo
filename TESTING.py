#linkedlist
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node

    def view(self):
        if not self.head:
            return 'Empty list'
        while self.head:
            print (self.head.data, end= '->') 
            self.head = self.head.next 
        print ('None')       
        return 
    
    def insert(self, prev_node, data):
        new_node = Node(data)
        current = self.head 
        while current:
            if prev_node == current.data:
                new_node.next = current.next 
                current.next = new_node
                break
            current = current.next 

            if current is None:
                print( "Me no hablas English")          

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node           

    def popstart(self):
        if self.head:
            self.head = self.head.next

    def popend(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None 


ll1 = linkedlist()
ll1.append(50)
ll1.append(60)
ll1.insert_start(500)
ll1.insert_start(600)
ll1.append(70)
ll1.insert(70, 40)
ll1.popstart()
ll1.popend()
ll1.view()    

'''

#stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
        new_node.next = self.top
        self.top = new_node

    def view(self):
        if self.top is None:
            raise Exception('no list da')    
        while self.top:
            print(self.top.data, end= '->')

s1 = stack()
s1.push(50)        
s1.view()    
