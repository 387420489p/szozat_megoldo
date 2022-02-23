words = []
dupla = []
with open("6_betus_szavak.txt", encoding="utf=8") as w:
    words = w.readlines()

for word in words:
    if "sz" in word or "cs" in word or "dz" in word or "gy" in word or "ly" in word or "ny" in word or "ty" in word or "zs" in word:
        dupla.append(word)

print(" ".join(dupla).lower())
