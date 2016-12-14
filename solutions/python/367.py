def how_much_coffee(events):
    occasions = 'cw', 'cat', 'dog', 'movie'
    count = 0
    for event in events:
        if event.lower() in occasions:
            if event.isupper():
                count += 1
            count += 1
    return count if count < 4 else 'You need extra sleep'