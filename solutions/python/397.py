def is_kiss(sentence):
    words = sentence.split()
    if all(len(word) <= len(words) for word in words):
        return 'Good work Joe!'
    return 'Keep It Simple Stupid'