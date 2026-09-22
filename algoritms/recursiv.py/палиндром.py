def is_palindrome(text):
    current_text = text.replace(',', '').replace(' ', '').replace(':', '').lower()
    left = 0
    right = len(current_text) - 1
    
    while left < right:
        if current_text[left] != current_text[right]:
            return False
        left += 1
        right -= 1
    return True
    





print(is_palindrome("А роза упала на лапу Азора"))  # True
print(is_palindrome("Привет"))                       # False
print(is_palindrome("шалаш"))                        # True
print(is_palindrome(""))                             # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True