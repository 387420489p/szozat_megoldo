#
wordlist = []
i = 0
with open("magyar-szavak.txt", encoding="utf=8") as r:
    words = r.readlines()

for word in words:
    word = word.strip()
    if len(word) == 5 and word.isalpha():
        if "sz" not in word and "cs" not in word and "dz" not in word and "gy" not in word and "ly" not in word and "ny" not in word and "ty" not in word and "zs" not in word:
            wordlist.append(word)
    elif len(word) == 6 and word.isalpha():
        if "sz" in word or "cs" in word or "dz" in word or "gy" in word or "ly" in word or "ny" in word or "ty" in word or "zs" in word:
            wordlist.append(word)
    elif len(word) == 7 and word.isalpha():
        for dupla in word:
            if "sz" in word:
                i += 1
            if "dz" in word:
                i += 1
            if "gy" in word:
                i += 1
            if "ly" in word:
                i += 1
            if "ny" in word:
                i += 1
            if "ty" in word:
                i += 1
            if "zs" in word:
                i += 1
            if "cs" in word:
                i += 1
            if i == 7*2:
                wordlist.append(word)
        i = 0
    else:
        pass

wordlist.sort()

with open("osszes_szo.txt", "w", encoding="utf-8") as w:
    w.write("\n".join(wordlist).lower())

print("\n".join(wordlist).lower())