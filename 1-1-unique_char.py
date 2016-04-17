def unique_chars(letters):
    while len(letters)>1:
        for l in letters[1:]:
            if l==letters[0]:
                return False
        letters=letters[1:]
    return True

print unique_chars('Molly')