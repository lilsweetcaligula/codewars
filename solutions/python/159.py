def most_frequent_item_count(collection):
    from collections import Counter
    return 0 if not collection else Counter(collection).most_common()[0][1]