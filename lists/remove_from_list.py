class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    # traversing a Linked List
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.next = self.head
        self.head = NewNode

    # function to remove a node
    def RemoveNode(self, RemoveKey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == RemoveKey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None


list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.head.next = e2
e2.next = e3

list.listprint()
print("--------")

list.RemoveNode("Tue")
list.listprint()
