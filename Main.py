class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    if root is None:
        root = BinaryTreeNode(new_value)
        return root
    
    elif root.data > new_value:
        if root.left_child is None:
            root.left_child = BinaryTreeNode(new_value)
            return root
        return insert(root.left_child,new_value)
    
    if root.right_child is None:
        root.right_child = BinaryTreeNode(new_value)
        return root
    return insert(root.right_child,new_value)

def inorder(root):
    print(*get_inorder(root),end = " ")

def preorder(root):
    print(*get_preorder(root),end = " ")

def postorder(root):
    print(*get_postorder(root),end = " ")
    
def get_inorder(root):
    if root is None:
        return []
    return get_inorder(root.left_child) + [root.data] + get_inorder(root.right_child)


def get_preorder(root):
    if root is None:
        return []
    return [root.data] + get_preorder(root.left_child) + get_preorder(root.right_child)


def get_postorder(root):
    if root is None:
        return []
    return get_postorder(root.left_child) + get_postorder(root.right_child) + [root.data]


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
