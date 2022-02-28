words = []
dupla = []
with open("magyar-szavak.txt", encoding="utf=8") as w:
    words = w.readlines()

szett = set(words)
abc_szett = sorted(szett)

print(*abc_szett)