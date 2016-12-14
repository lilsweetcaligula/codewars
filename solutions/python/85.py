def validate_hello(greetings):
    lookup = { 'hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc' }
    words = [
        ''.join(char for char in word if char.isalpha()) 
            for word in greetings.split()
    ]
    for word in words:
        if word.lower() in lookup:
            return True
    return False