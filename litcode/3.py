def invert_case(s):
    new_letter = []
    for letter in s:
        if letter.islower():
            new_letter.append(letter.upper())
        else:
            new_letter.append(letter.lower())
        
    return f'{''.join(new_letter)}'




print(invert_case('www.Python-Academy.org'))
# вернёт 'WWW.pYTHON-aCADEMY.ORG'