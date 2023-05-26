def _swap(t, a, b):
    k = t[a]
    t[a] = t[b]
    t[b] = k

def selection_sort(t):
    n = len(t)

    for i in range(0,n):
        minus = i

        for j in range(i+1, n):
            if t[j] < t[minus]: minus = j

        _swap(t, i, minus)

    return t

def _insert_action(t, gap = 1):
    for i in range(gap, len(t)):
        for j in range(i, gap-1, -gap):
            if t[j] < t[j-gap]:
                _swap(t, j, j-gap)

    return t


def insertion_sort(t):
    _insert_action(t)

    return t

def shell_sort(t):
    gap = len(t)

    while (gap:= gap//2) >= 1:
        _insert_action(t, gap)

    return t

def bubble_sort(t):
    n = len(t)
    swapped = True
    while swapped:
        swapped = False

        for i in range(1,n):
            if t[i] < t[i-1]:
                _swap(t, i, i-1)
                swapped = True

        n -= 1

    return t

def quick_sort(t, first = 0, last = None):
    if not last: last = len(t)-1

    if first < last:
        pivot = last
        j = first

        for i in range(first, pivot):
            if t[i] < t[pivot]:
                _swap(t, i,j)
                j += 1

        _swap(t, pivot, j)

        quick_sort(t, first, j-1), quick_sort(t, j+1, last)

    return t

def merge(a,b):
    i,j = 0,0
    merged_list = []

    while i < len(a) and j < len(b):

        if (a[i] <= b[j]):
            merged_list.append(a[i])
            i += 1

        else:
            merged_list.append(b[j])
            j += 1

    merged_list.extend(a[i:])
    merged_list.extend(b[j:])

    return merged_list

def merge_sort(t):
    n = len(t)

    if n <= 1:
        return t
    
    m = n//2
    first = t[:m]
    last = t[m:]

    return merge(merge_sort(first), merge_sort(last))