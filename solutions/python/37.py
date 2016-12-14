class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if head == None:
        return None
    slow = head
    fast = head.next
    while fast != None:
        if slow.data != fast.data:
            slow.next = fast
            slow = slow.next
        else:
            fast = fast.next
    slow.next = None
    return head