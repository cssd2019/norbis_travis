


def is_number(value):
    ''' check if value is either an int or float '''
    if (isinstance(value, int) or
        isinstance( value, float )):

        return True

    return False


def are_numbers(*values):
    ''' check if value is either an int or float '''

    for value in values:
        if ( not is_number( value )):
             return False

    return True

    


def sum_numbers( value1, value2):
    if are_numbers( value1,value2):
        return value1 + value2

    raise TypeError('one or both of the values provided are not numbers')


def sum_vectors( vector1, vector2):

    summed_vector = []

    for value1, value2 in zip( vector1, vector2):
        summed_vector.insert(0, value1 + value2 )

    return summed_vector



