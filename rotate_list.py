def rotate_right(lst, k):
    """
    Rotates a list to the right by k elements.
    """
    return lst[-k:] + lst[:-k]

def rotate_left(lst, k):
    """
    Rotates a list to the left by k elements.
    """
    return lst[k:] + lst[:k]

def rotate_list(lst, k):
    """
    Rotates a list to the left or right by k elements.
    """
    return lst[-k:] + lst[:-k]