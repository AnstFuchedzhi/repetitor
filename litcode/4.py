def wrap_text(s, width):
    new_list = []
    for letter in range(0, len(s), width):
        new_list.append(s[letter : letter + width])
    return '\n'.join(new_list)
    





print(wrap_text('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))
# вернёт 'ABCD\nEFGH\nIJKL\nMNOP\nQRST\nUVWX\nYZ'