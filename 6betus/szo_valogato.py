words = []
letter = "a"
position = 1
wordlist = []
with open("magyar-szavak.txt", encoding="utf=8") as r:
    words = r.readlines()

for word in words:
    if len(word) == 6:
        if "sz" not in word and "cs" not in word and "dz" not in word and "gy" not in word and "ly" not in word and "ny" not in word and "ty" not in word and "zs" not in word:
            wordlist.append(word)
    elif len(word) == 7:
        if "sz" in word or "cs" in word or "dz" in word or "gy" in word or "ly" in word or "ny" in word or "ty" in word or "zs" in word:
            wordlist.append(word)
    else:
        pass

wordlist.sort()

with open("osszes_szo.txt", "w", encoding="utf-8") as w:
    w.write("".join(wordlist).lower())

print("".join(wordlist).lower())
