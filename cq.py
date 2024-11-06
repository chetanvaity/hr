class Queue:
    def __init__(self, size):
        self.arr = [None] * size
        self.start = 0
        self.end = 0
        self.size = size
        self.numObj = 0
            
    def add(self, obj):
        if self.isFull():
            raise Exception("Queue full, cannot add, size=%d, numObj=%d" % (self.size, self.numObj))
        self.arr[self.start] = obj
        self.start = self.start + 1
        if (self.start >= self.size):
            self.start = 0
        self.numObj = self.numObj + 1
        
    def remove(self):
        if self.isEmpty():
            raise Exception("Queue is empty, cannot remove")
        ret = self.arr[self.end]
        self.arr[self.end] = None
        self.end = self.end + 1
        if (self.end >= self.size):
            self.end = 0
        self.numObj = self.numObj - 1
        return ret
    
    def isFull(self):
        if (self.numObj >= self.size):
            return True
        return False
#        if (self.start) % self.size == self.end:
#            return True
#        return False
    
    def isEmpty(self):
        if (self.numObj <=0):
            return True
        return False
#        if (self.end) % self.size == self.start:
#            return True
#        return False
    
    def printQ(self):
        print self.arr
        print "start=%d, end=%d" % (self.start, self.end)
        
q = Queue(3)
q.add('a')
q.add('b')
q.add('c')
q.remove()
q.add('d')
q.remove('e')
q.printQ()
