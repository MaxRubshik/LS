def to_alternating_case(string):
    temp = ""
    for character in string:
        if character.isupper() == True:
            temp += character.lower()
        else:
            temp += word.upper()
    return temp
