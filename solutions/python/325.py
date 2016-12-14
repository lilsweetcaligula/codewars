class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    if node and index >= 0:
        if index == 0:
            return node
        return get_nth(node.next, index - 1)
    raise IndexError()
  class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    if (index < 0) or (index >= 0 and node == None):
        raise IndexError()
    if index == 0: 
        return node
    return get_nth(node.next, index - 1)
  