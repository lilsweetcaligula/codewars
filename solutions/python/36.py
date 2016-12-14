class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source == None:
        raise ValueError('source cannot be None')
    new_first, source = source, source.next
    new_first.next = dest
    dest = new_first
    return Context(source, dest)