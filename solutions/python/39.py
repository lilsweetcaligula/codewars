class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def append(listA, listB):
    dummy = node = Node(0, listA)
    while node.next:
        node = node.next
    node.next = listB
    return dummy.next