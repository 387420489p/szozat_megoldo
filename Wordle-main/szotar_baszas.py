words = []
wordlist = []
letter = "a"
position = 1
with open('szavak.txt', encoding="utf=8") as w:
  words = w.readlines()
while letter!='':
  del wordlist[:]
  for word in words:
    if "sz" in word:

