def is_float(x):
    '''
        This function takes a string as parameter and checks whether it is a Number or not (Integer or Float).
    '''
    try:
        # only integers and float converts safely
        num = float(x)
        return True
    except ValueError as e: # not convertable to float
        return False