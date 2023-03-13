class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addElementHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def addElementTail(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    
    def maju(self, n):
        current = self.head
        for i in range(n):
            if current is None:
                break
            current = current.next
        if current is not None:
            print(current.data)
            self.head = current
    
    def mundur(self, n):
        current = self.head
        for i in range(n):
            if current is None:
                break
            current = current.prev
        if current is not None:
            print(current.data)
            self.head = current

# contoh penggunaan
linkedlist = LinkedList()
linkedlist.addElementHead("Jogja") #Jogja
linkedlist.addElementHead("Jakarta") ##Jakarta - Jogja
linkedlist.addElementTail("Bali") #Jakarta - Jogja - Bali
linkedlist.addElementTail("Bandung") #Jakarta - Jogja - Bali - Bandung
linkedlist.maju(2) #output: Bali
linkedlist.mundur(1) #output: Jogja
linkedlist.maju(5) #output: Bali
linkedlist.mundur(3) #output: Bandung
