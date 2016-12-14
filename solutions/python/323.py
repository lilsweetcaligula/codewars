def transpose(song, interval):
    sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    flat  = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    transposed = []
    for note in song:
        try:
            index = sharp.index(note)
        except ValueError:
            index = flat.index(note)
        transposed.append(sharp[(index + interval) % len(sharp)])
    return transposed