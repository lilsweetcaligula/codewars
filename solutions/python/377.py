def count_sheeps(arrayOfSheeps: list) -> int:
    return len(list(filter(lambda sheepIsPresent : sheepIsPresent, arrayOfSheeps)))