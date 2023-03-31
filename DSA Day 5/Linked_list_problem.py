#program to merge two linked lists such that list2 is merged ith list1 after n number of nodes
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def merge_lists(self, list1, list2, n):
        current_node = list1.head
        for i in range(n-1):
            if not current_node:
                return "List1 is short!"
            current_node = current_node.next
        if not current_node:
            return "List1 is short!"
        temp = current_node.next
        current_node.next = list2.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = temp

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# create first linked list
list1 = LinkedList()
list1.insert(1)
list1.insert(2)
list1.insert(4)
list1.insert(3)
list1.insert(5)

# create second linked list
list2 = LinkedList()
list2.insert(9)
list2.insert(8)
list2.insert(11)

# merge list2 with list1 after n=2 nodes
list1.merge_lists(list1, list2, 2)

# display merged linked list
list1.display()
