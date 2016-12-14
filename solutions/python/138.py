def get_grade(*grades):
    return ['F', 'F', 'F', 'F', 'F', 'F', 
            'D', 'C', 'B', 'A', 'A'][(sum(grades) // len(grades)) // 10]