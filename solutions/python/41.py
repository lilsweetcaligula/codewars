class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def sorted_insert(head, data):
    dummy = Node(0, head)
    node = dummy
    while node.next and data > node.next.data:
        node = node.next
    old_next = node.next
    node.next = Node(data, old_next)
    return dummy.next