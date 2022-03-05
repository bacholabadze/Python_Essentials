def checkComprise(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.lower()

    letters = set(word1)
    for ch in letters:
        if word2.find(ch) == -1:
            return 'No'
    return 'Yes'


print(checkComprise('donor', 'Nabucodonosor'))  # yes
print(checkComprise('donut', 'Nabucodonosor'))  # no

print(checkComprise('dog', 'vcxzxduybfdsobywuefgas'))  # yes
print(checkComprise('dog', 'vcxzxdcybfdstbywuefsas'))  # no
