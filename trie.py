class node:
    def __init__(self):
        self.children = {}
        self.isLastChar = False
        self.total = 0

def addWord(root, w):
    n = root
    length = len(w)
    for i in xrange(length):
        c = w[i]
        n.total = n.total + 1
        if n.children.get(c) is None:
            n.children[c] = node()
        n = n.children[c]
        if i == (length - 1):
            n.isLastChar = True


def printPreOrder(n):
    print ' '.join(n.children.keys())
    print n.total
    for k in n.children.keys():
        printPreOrder(n.children[k])


def findLastNode(root, w):
    n = root
    for c in w:
        if n.children.get(c) is None:
            return None
        n = n.children[c]
    return n


root = node()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        addWord(root, contact)
    elif op == 'print':
        printPreOrder(root)
    elif op == 'find':
        ln = findLastNode(root, contact)
        if ln is None:
            print 0
        else:
            print ln.total
