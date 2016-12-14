to_alternating_case = (lambda string: "".join(
        char.upper() if char.islower() else char.lower() 
        for char in string))