class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def push(head, data):
    dummy = Node(0, head)
    old_next = dummy.next
    dummy.next = Node(data, old_next)
    return dummy.next    
  
def build_one_two_three():
    node = None
    for data in (3, 2, 1):
        node = push(node, data)
    return node