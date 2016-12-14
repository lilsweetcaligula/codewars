def given_nth_value(arr, k, str_):
    #your code here
    #return "Incorrect value for k"
    #return "Valid entries: 'max' or 'min'"
    #return "No values in the array"
    #return "Invalid entry list"
    #return k-th term
    try:
        cmds = { 
            'min': lambda arr: arr, 
            'max': lambda arr: reversed(arr) 
        }
    
        if not isinstance(k, int) or k < 0:
            raise TypeError()
        if str_.lower() not in cmds:
            raise KeyError()
        if not 0 < k < len(arr):
            raise IndexError()        
        if not all(isinstance(value, int) for value in arr):
            raise ValueError()
            
        data = list(cmds[str_.lower()](sorted(set(arr))))
        return data[k - 1]
        
    except KeyError:
        return "Valid entries: 'max' or 'min'"
    except ValueError:
        return 'Invalid entry list'
    except IndexError:
        return ['No way', 'No values in the array'][len(arr) == 0]
    except TypeError:
        return 'Incorrect value for k'