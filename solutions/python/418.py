def find_even_index(array):
    leftSum, rightSum = 0, sum(array)
    for index, value in enumerate(array):
        leftSum  += value        
        if leftSum == rightSum: 
            return index
        else:
            rightSum -= value
    return -1