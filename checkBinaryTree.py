""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    inList = inOrder(root)

    if len(inList) < 2:
        return True
    
    for i in xrange(len(l) - 1):
        if inList[i] >= inList[i+1]:
            return False

    return True


inList = []

def inOrder(root):
    if (root is None):
        return
    if (root.left is not None):
        inOrder(root.left)
    inList.append(root.data)
    if (root.right is not None):
        inOrder(root.right)
