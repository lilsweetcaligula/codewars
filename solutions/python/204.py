def list_to_array(lst, extend = None):
    extend = extend or []
    if lst: 
        extend.append(lst.value)
        list_to_array(lst.next, extend)
    return extend
    