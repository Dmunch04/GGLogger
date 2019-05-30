import GG

@GG.Print
@GG.Combine (str, int)
def Test ():
    if 1:
        return 'Hello'
        
    else:
        return 1

@GG.Int
def Test ():
    return 1

@GG.Float
def Test ():
    return 1.0

@GG.String
def Test ():
    return '1'

@GG.List
def Test ():
    return [1]

@GG.Dict
def Test ():
    return {'1': 0}

@GG.Tuple
def Test ():
    return (1, 0)

@GG.Int
@GG.Log ()
def Test ():
    return '1'
