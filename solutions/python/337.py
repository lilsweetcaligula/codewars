partlist = (lambda sequence, separator = " ":
            [(separator.join(sequence[:index]), separator.join(sequence[index:])) 
                for index in range(1, len(sequence))])