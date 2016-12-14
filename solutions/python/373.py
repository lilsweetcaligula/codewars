def word_search(query, seq):
    return [string for string in seq if string.lower().find(query.lower()) >= 0] or ['None']