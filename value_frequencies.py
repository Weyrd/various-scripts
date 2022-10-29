from collections import defaultdict

def value_frequencies(values):
    """
    It takes a list of values and returns a dictionary of value frequencies
    
    :param values: a list of values
    :return: A dictionary of value frequencies.
    """
    frequencies = defaultdict(int)
    
    for value in values:
        frequencies[value] += 1

    return frequencies