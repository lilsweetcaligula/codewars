def cypher(string):
    return(string
        .translate(
            str.maketrans('IREASGTBO', '123456780'))
        .translate(
            str.maketrans('lzeasbtgo', '123456790')))