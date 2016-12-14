def sum_from_string(string):
    parsed = "".join(char if char.isdigit() else ' ' for char in string)
    numbers = [int(number) for number in parsed.split()]
    return sum(numbers) if numbers else 0def sum_from_string(string):
    parsed = "".join(char if char.isdigit() else ' ' for char in string)
    numbers = [int(number) for number in parsed.split()]
    if numbers:
        return sum(numbers)
    return 0
    def sum_from_string(string):
    import re
    numbers = re.findall('(\d+)', string)
    if numbers:
        return sum(int(number) for number in numbers)
    return 0