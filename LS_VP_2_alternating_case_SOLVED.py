test = "AltERNating"

def to_alternating_case(string):
    res = ""
    for word in string:
        if word.isupper() == True:
            res = res + word.lower()
        else:
            res = res + word.upper()
    return res


print(to_alternating_case(test))
