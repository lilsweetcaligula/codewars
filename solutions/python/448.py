#Remember you have a CHANGE dictionary to work with ;)

def change_count(change):
    return '${:.2f}'.format(sum(CHANGE[coin] for coin in change.split()))