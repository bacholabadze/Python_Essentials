def checkAnagrams(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    for ch in text1:
        if not text1.count(ch) == text2.count(ch):
            return "Not anagrams"
    return "Anagrams"


print(checkAnagrams("Listen", "Silent"))  # True
print(checkAnagrams("rail SaFety", "fairy Tales"))  # True
print(checkAnagrams("Putin Khuilo", "Glory To Ukraine"))  # False
