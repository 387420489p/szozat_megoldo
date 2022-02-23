words = []
letter="a"
position=1
wordlist=[]
with open('szavak.txt', encoding="utf=8") as w:
  words = w.readlines()
while letter!='':
  del wordlist[:]
  letter=input("Milyen betűt ismersz? ")
  color=input("Milyen színű? (S,Z,F): ")
  if color == 'z' or color == 'Z' or color == 's' or color == 'S':
    position=int(input("Hányadik helyen áll? (1-5)"))-1
  for word in words:
    if color == 'z' or color == 'Z':
      if word[position]==letter:
        wordlist.append(word)
    elif color == 'f' or color == 'F':
      if letter not in word:
        wordlist.append(word)
    elif color == 's' or color == 'S':
      if letter in word:
        if word[position]!=letter:
          wordlist.append(word)
  words=wordlist.copy()
  print(*wordlist)
  print(f"Lehetséges helyes szavak: {len(words)} db")
