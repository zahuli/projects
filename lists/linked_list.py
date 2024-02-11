# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
# https://www.geeksforgeeks.org/python-linked-list/


# create a Node clas

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


list = SLinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list.head.next = e2

# Link second Node to third node
e2.next = e3

list.listprint()
