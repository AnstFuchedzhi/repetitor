word = input('Введите слово: ')
revers_word = ''
for symbol in word:
    revers_word = symbol + revers_word
if word == revers_word:
    print('Это палиндром')
else:
    print('Нет')        
    

    










