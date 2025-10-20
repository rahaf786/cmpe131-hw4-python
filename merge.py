# merge.py
def merge_list(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Inputs must be lists")
    for x in a + b:
        if not isinstance(x, int):
            raise TypeError("All elements must be integers")
    arr = a + b
    for i in range(1, len(arr)):            # insertion sort
        key = arr[i]; j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]; j -= 1
        arr[j+1] = key
    return arr
