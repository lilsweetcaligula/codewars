pattern = (lambda count:
             '\n'.join(''.join(str(value) for value in reversed(range(times, count + 1)))
                     for times in reversed(range(1, count + 1))))