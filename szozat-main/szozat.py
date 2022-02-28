def szozat():
  print("Ez a program segít megoldani a Szózat nevű játékot.\nhttps://szozat.miklosdanka.com/\nTedd meg az első tipped a játékban és írd be az ismert betűket a megfelelő színnel.\nAhhoz, hogy a program jól működjön legalább 2 betűt meg kell adnod!")
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

#double letters to numbers
  for word in words:
    new_word = word.replace("cs", "1").replace("sz", "2").replace("ty", "3").replace("dz", "4").replace("gy", "5").replace("ly", "6").replace("ny", "7").replace("zs", "8")
    new_words.append(new_word)

#inputs, exceptions
  while letter!='':
    del wordlist[:]
    letter=input("Milyen betűt ismersz? ")
    while letter not in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "í", "é", "á", "ű", "ő", "ú", "ö", "ü", "ó", "cs", "sz", "ty", "dz", "gy", "ly", "ny", "zs"]:
      print(f"A(z) {letter} nem egy betű, próbáld újra!")
      letter = input("Milyen betűt ismersz? ")

#double character exceptions
    while letter in ["cs", "sz", "ty", "dz", "gy", "ly", "ny", "zs"]:
      if letter == "cs":
        letter = "1"
      elif letter == "sz":
        letter = "2"
      elif letter == "ty":
        letter = "3"
      elif letter == "dz":
        letter = "4"
      elif letter == "gy":
        letter = "5"
      elif letter == "ly":
        letter = "6"
      elif letter == "ny":
        letter = "7"
      elif letter == "zs":
        letter = "8"
      else:
        pass
#--------------------

    color=input("Milyen színű? (S,Z,F): ")
    while color not in ["F", "f", "Z", "z", "S", "s"]:
      print(f"A(z) {color} nem a szín kezdőbetűje. Kérlek írd be a helyes szín kezdőbetűjét! (s, f, z)")
      color = input("Milyen színű? (S, Z, F vagy s, z, f) ")
    if color == 'z' or color == 'Z' or color == 's' or color == 'S':
      position=int(input("Hányadik helyen áll? (1-5)" ))-1


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

#back from number to letter
    for new_word in new_words:
      vissza_word = new_word.replace("1", "cs").replace("2", "sz").replace("3", "ty").replace("4 ", "dz").replace("5", "gy").replace("6", "ly").replace("7", "ny").replace("8", "zs")
      vissza_words.append(vissza_word)
      vissza_words.remove(new_word)
      wordlist = vissza_words

    print(*wordlist)
    print(f"Lehetséges helyes szavak: {len(new_words)} db")

    if len(new_words) < 1:
      print("Sajnos a szó nincs benne a program szótárában. ¯\_(ツ)_/¯")


szozat()
