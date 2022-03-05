text = input("Enter text: ")
shift = int(input("Shift value: "))

cipher = ""
for ch in text:
    if not ch.isalpha():
        cipher += ch
        continue

    if ch.islower():
        code = ord(ch) + shift
        if code > ord('z'):
            code = ord('a') + code - ord('z') - 1
    else:
        code = ord(ch) + shift
        if code > ord('Z'):
            code = ord('A') + code - ord('Z') - 1
    cipher += chr(code)
print(cipher)