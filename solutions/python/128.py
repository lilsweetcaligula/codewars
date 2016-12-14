def DNAtoRNA(dna):
    return dna.translate(str.maketrans('GCATgcat', 'GCAUgcau'))