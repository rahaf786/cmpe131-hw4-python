# sorted.py
def reverse_sort_dictionary(d):
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary")
    out = []
    for name, val in d.items():
        if not isinstance(name, str) or not (isinstance(val, tuple) and len(val) == 2):
            raise TypeError("Expect {str: (phone, age)}")
        phone, _age = val
        if not isinstance(phone, int):
            raise TypeError("Phone must be int")
        out.append((name, phone))
    out.sort(key=lambda t: t[0], reverse=True)
    return out
