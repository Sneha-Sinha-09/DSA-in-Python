#Traversing a linked list

class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")

#link first Node to second Node
list.headval.nextval=e2
e2.nextval=e3
list.listprint()


#Add an element at the beginning
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    def AtBegining(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode

list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.AtBegining("Sun")
list.listprint()


#Add new element at the end
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class SLinkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    def AtBegining(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode

    def AtEnd(self,newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        laste=self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode

list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.AtBegining("Sun")
list.AtEnd("Fri")
list.Inbetween(list.headval.nextval,"Thu")
list.listprint()


class Node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.start_node=None
        
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
        else:
            n=self.start_node
            while n is not None:
                print(n.item," ")
                n=n.ref
                
    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.ref=self.start_node
        self.start_node=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
        while n.ref is not None:
            n=n.ref
        n.ref=new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node=self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        n=self.start_node
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None

    def delete_element_by_value(self,x):
        if self.start_node is None:
            print("List has no element")
            return
        if self.start_node.item==x:
            self.start_node=self.start_node.ref
            return
        
        n=self.start_node
        while n.ref is not None:
            if n.ref.item==x:
                break
            n=n.ref

        if n.ref is None:
            print("Item is not found in the list")
        else:
            n.ref=n.ref.ref

    def search_item(self,x):
        if self.start_node is None:
            print("List has no elements")
            return
        n=self.start_node
        while n is not None:
            if n.item==x:
                print("Item found")
                return True
            n=n.ref
        print("Item not found")
        return False
    
    def get_count(self):
        if self.start_node is None:
            return 0
        n=self.start_node
        count=0
        while n is not None:
            count=count+1
            n=n.ref
        return count
    
    def insert_at_index(self,index,data):
        if index==1:
            new_node=Node(data)
            new_node.ref=self.start_node
            self.start_node=new_node
        i=1
        n=self.start_node
        while i<index-1 and n is not None:
            n=n.ref
            i=i+1
        if n is None:
            print("Index out of bound")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
            

new_linked_list=LinkedList()
new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(25)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(35)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(45)
new_linked_list.traverse_list()
new_linked_list.delete_at_start()
print("After deletion at the beginning")
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
print("After deletion at the end")
new_linked_list.traverse_list()
new_linked_list.delete_element_by_value(30)
print("After deleting 30")
new_linked_list.traverse_list()
new_linked_list.search_item(5)
new_linked_list.search_item(25)
print("The number of nodes",new_linked_list.get_count())
new_linked_list.insert_at_index(3,8)
new_linked_list.traverse_list()






    






























            
