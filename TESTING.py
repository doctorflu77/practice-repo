class Node:
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
        return

    def view(self):    
        current = self.head 
        while current:
            print (current.data, end= '->')
            current = current.next
        print (None)    
        return    

ll1 = linkedlist()

ll1.append(10)
ll1.append(20)
ll1.append(30)
ll1.view()
