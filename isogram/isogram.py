def is_isogram(string):
    newstring = string.lower().replace('-', '').replace(' ', '')
    for letter in newstring:
        if newstring.count(letter) > 1: return False
    return True
