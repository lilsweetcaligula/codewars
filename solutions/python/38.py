class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def insert_nth(head, index, data):
    dummy = node = Node(0, head)
    while index > 0:
        if node == None:
            raise IndexError()
        else:
            node = node.next
            index -= 1
    old_next = node.next
    node.next = Node(data, old_next)
    return dummy.next