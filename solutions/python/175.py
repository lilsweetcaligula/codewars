def openOrSenior(data):
    return [['Open', 'Senior'][datum[0] >= 55 and datum[1] > 7] for datum in data]