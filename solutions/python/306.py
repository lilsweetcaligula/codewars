func = lambda n: n % 2 == 0

def map(arr, somefunction):
    try:
        return [somefunction(int(value)) for value in arr]
    except ValueError:
        return 'array should contain only numbers'
    except TypeError:
        if not hasattr(somefunction, '__call__'):
            return 'given argument is not a function'
        raise