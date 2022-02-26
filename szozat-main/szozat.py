def szozat():
  words = []
  letter="a"
  position=1
  wordlist=[]
  new_words = []
  vissza_words = []
  vissza_wordlist = []
  with open('szavak.txt', encoding="utf=8") as w:
    words = w.readlines()
  new_words = vissza_words

#Ez változtatja át a kettős karaktereket számokra
  for word in words:
    new_word = word.replace("cs", "1")
    new_words.append(new_word)

#inputs, exceptions
  while letter!='':
    del wordlist[:]
    letter=input("Milyen betűt ismersz? ")
    while letter not in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "í", "é", "á", "ű", "ő", "ú", "ö", "ü", "ó"]:
      print(f"A(z) {letter} nem egy betű, próbáld újra!")
      letter = input("Milyen betűt ismersz? ")
    color=input("Milyen színű? (S,Z,F): ")
    while color not in ["F", "f", "Z", "z", "S", "s"]:
      print(f"A(z) {color} nem a szín kezdőbetűje. Kérlek írd be a helyes szín kezdőbetűjét! (s, f, z)")
      color = input("Milyen színű? (S, Z, F vagy s, z, f) ")
    if color == 'z' or color == 'Z' or color == 's' or color == 'S':
      position=int(input("Hányadik helyen áll? (1-5)"))-1

#magic word finder and sorter
    for word in new_words:
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
    new_words=wordlist.copy()

    #vissza 1-ből cs-be
    for word in new_words:
      vissza_word = word.replace("1", "cs")
      vissza_words.append(vissza_word)
      vissza_words.remove(word)
      wordlist = vissza_words

    print(*wordlist)
    print(f"Lehetséges helyes szavak: {len(new_words)} db")

    if len(new_words) < 1:
      print("Sajnos a szó valószínűleg kettős betűt (sz, cs, gy...) tartalmaz, amit egyelőre nem támogat a program. \nVagy nincs benne a program szótárában. ¯\_(ツ)_/¯")
      #uj_szotar = print(input("Úgy néz ki nincs a szó a szótárban, vagy dupla betű (sz, gy, stb...) van benne. Szeretnéd megpróbálni a dupla betűs szótárral? I/N "))
      #if uj_szotar == "I":
        #print("oké próbáljuk meg!")
      #else:
        #print("rip. legalább a funkció működik. (:")

szozat()
