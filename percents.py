def percents(x, y):
    """What percentage of x is y"""
    one_persent = x / 100
    reslt = y / one_persent
    return reslt

def print_percents (x, y):
    """Print percentage of x is y"""
    print(str(y) + " is " + str(percents(x, y)) + "% of " +str(x))


percents(200, 50)