spin_words = (lambda sentence:
    ' '.join(word if len(word) < 5 else word[::-1] for word in sentence.split()))