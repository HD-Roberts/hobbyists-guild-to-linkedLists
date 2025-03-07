#creates a node object 
class llNode: 
    def __init__(self, data ):
        self.data = data
        self.next = None

#creates the a linkedlist object to contain nodes and manipulate nodes 
class linkedList:

    #initalises the linked list 
    def __init__(self):
        self.head = llNode(None)

    #adds a node to the end of the linked list in O(n) time 
    def append(self, data):

        #declare variables 
        newNode = llNode(data)
        currentNode = self.head

        #moves node pointer to last node in the linked list 
        while currentNode.next is not None:
            currentNode = currentNode.next 

        #makes the final node point to the new node appended to the end 
        currentNode.next = newNode
    
    #adds a node to the start of the linked list in 0(1) time 
    def appendStart(self, data):
        newNode = llNode(data)

        #makes variables for the head node and the node it points to
        headNode = self.head
        headNodeNext = self.head.next

        #makes the head point to the inserted node and the inserted node point to the second node 
        headNode.next = newNode
        newNode.next = headNodeNext
    
    #outputs the linked list as a string 
    def print(self):
        linkedListString = ""
        currentNode = self.head.next

        #iterates though nodes untill the end of the linkedlist is reached 
        while currentNode is not None:

            #makes sure formatation is correct in output string 
            if currentNode.next == None: 
                linkedListString += str(currentNode.data)
            else: 
                linkedListString += str(currentNode.data) + " --> "

            currentNode = currentNode.next
        
        print(linkedListString)





#example opperations 
linkedListInstance = linkedList()
linkedListInstance.append(5)
linkedListInstance.append(5)
linkedListInstance.appendStart(10)
linkedListInstance.print()
