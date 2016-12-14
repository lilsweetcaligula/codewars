class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node, currLength = 0):
    if node:
        return length(node.next, currLength + 1)
    return currLength
  
def count(node, data, currCount = 0):
    if node:
        if node.data == data: 
            currCount += 1
        return count(node.next, data, currCount)
    return currCountclass Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
length = (lambda node, count = 0: 
    length(node.next, count + 1) if node else count)
  
count = (lambda node, data, occurs = 0:
    occurs if not node 
    else count(node.next, data, occurs + 1) if node.data == data
    else count(node.next, data, occurs))