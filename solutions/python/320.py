remove_smallest = (lambda numbers: 
    numbers if numbers and not (lambda L: L.remove(min(L)))(numbers) 
    else [])