# from DeepSeek

# Node Class
# Each node stores:
#     Data (value)
#     Next (reference to the next node)

class Node:
    def __init__(self, data=None):
        self.data = data  # Value stored in node
        self.next = None  # Pointer to next node (initially None)


class LinkedList:
    def __init__(self):
        self.head = None  # First node in the list (initially empty)

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link new node at the end

    # Print the list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Create a linked list: 1 -> 2 -> 3 -> None
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
