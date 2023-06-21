import os

def to_roman_num(num):
    """
    It takes a number and returns a string of the roman numeral representation of that number
    
    :param num: The number to be converted to Roman numerals
    :return: the roman numeral equivalent of the number passed to it.
    """
    num_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    result = ''

    for value, roman in num_roman:
        (d, num) = divmod(num, value)
        result += roman * d

    return result

nbr = int(input("Numeral number: "))
print(f"Roman number: {to_roman_num(nbr)}")
os.system('pause')
