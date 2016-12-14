import string

DNA_strand = lambda dna: dna.translate(string.maketrans('ATGCatgc', 'TACGtacg'))