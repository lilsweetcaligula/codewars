def decodeMorse(morseCode):
    words = morseCode.strip().split('   ')
    return ' '.join(''.join(MORSE_CODE.get(char, char) for char in word.split()) for word in words)