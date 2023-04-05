class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        if not self.occupied_table_list:
            self.occupied_table_list.append(1)
        else:
            for i in range(len(self.occupied_table_list)):
                if i == len(self.occupied_table_list) - 1:
                    self.occupied_table_list.append(self.occupied_table_list[-1]+1)
                elif self.occupied_table_list[i+1] - self.occupied_table_list[i] > 1:
                    self.occupied_table_list.insert(i+1, self.occupied_table_list[i]+1)
                    break

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
            
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def reverse_list(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


# create a BakeHouse object
bh = BakeHouse()

# allocate tables
bh.allocate_table()
bh.allocate_table()
bh.allocate_table()
bh.allocate_table()

# print occupied table list
print(bh.get_occupied_table_list())

# deallocate a table
bh.deallocate_table(2)

# allocate a new table
bh.allocate_table()

# print occupied table list
print(bh.get_occupied_table_list())

# create a linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# print original list
ll.print_list()

# reverse the list
ll.reverse_list()

# print reversed list
ll.print_list()
