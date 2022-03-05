def checkPalindrome(text):
    text = text.lower().replace(" ", "")
    for ix in range(0, int(len(text)/2)):
        # print(text[ix], text[-ix - 1])
        if not text[ix] == text[-ix-1]:
            return "It's not a palindrome"
    return "It's a palindrome"


print(checkPalindrome("Ten animals I slam in a net"))  # True
print(checkPalindrome("Cat Tac"))  # True
print(checkPalindrome("KayAk"))  # True
print(checkPalindrome("Palindrome"))  # False
