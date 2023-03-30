#Traversing a tree
class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end='')

def preorder(root):
    if root:
        #Traverse root
        print(str(root.val) + "->", end='')
        #Traverse left
        preorder(root.left)
        #Traverse right
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder Traversal:")
inorder(root)
print("\n Preorder Traversal:")
preorder(root)
print("\n Postorder traversal:")
postorder(root)




#Insert a root
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(node,data):
    if node is None:
        return Node(data)
    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)
    return node
     
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data)+"->",end="")
        inorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data)+"->",end="")
#Depth First Search
def preorder(root):
    if root:
        print(str(root.data)+"->",end="")
        preorder(root.left)
        preorder(root.right)

root  = None
root = insert(root,10)
root = insert(root,11)
root = insert(root,12)
root = insert(root,13)
root = insert(root,14)
root = insert(root,15)
root = insert(root,16)
root = insert(root,17)
root = insert(root,18)
root = insert(root,19)
inorder(root)













