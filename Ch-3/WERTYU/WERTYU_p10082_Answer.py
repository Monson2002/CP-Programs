s = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
while True:
    try:
        s2 = input()
    except EOFError:
        break
    for i in range(len(s2)):
        for j in range(len(s)):
            if s2[i] == s[j]:
                s2 = s2[:i] + s[j-1] + s2[i+1:]
                break
    print(s2)
