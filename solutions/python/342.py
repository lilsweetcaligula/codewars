def mean(lst):
    integers = [int(value) for value in filter(lambda item: item.isdigit(), lst)]
    characters = [character for character in filter(lambda item: item.isalpha(), lst)]
    return [sum(integers) / float(len(integers)), "".join(characters)]
    