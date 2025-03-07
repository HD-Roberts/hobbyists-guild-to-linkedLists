class llNode: 
    def __init__(self, data ):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = llNode(None)


    def append(self, data):
        newNode = llNode(data)
        currentNode = self.head

        while currentNode.next is not None:
            currentNode = currentNode.next 

        currentNode.next = newNode
    

    def appendStart(self, data):
        newNode = llNode(data)

        headNode = self.head
        headNodeNext = self.head.next

        headNode.next = newNode
        newNode.next = headNodeNext
    

    def print(self):
        linkedListString = ""
        currentNode = self.head.next

        while currentNode is not None:

            if currentNode.next == None: 
                linkedListString += str(currentNode.data)
            else: 
                linkedListString += str(currentNode.data) + " --> "

            currentNode = currentNode.next
        
        print(linkedListString)






linkedListInstance = linkedList()
linkedListInstance.append(5)
linkedListInstance.append(5)
linkedListInstance.appendStart(10)
linkedListInstance.print()
