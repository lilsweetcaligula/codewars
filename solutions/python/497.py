def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    return sorted(value ** 2 for value in array1) == sorted(array2)
	