#coding: utf8
import random
HANGMAN= (
"""
 ------
 |    |
 |    |
 |
 |
 |
 |
 |
 |
 |
 |
-------
""" ,
"""
 ------
 |    |
 |    |
 |    O  |
 |       |
 |
 |
 |
 |
 |
 |
 |
-------
""" ,
"""
 ------
 |    |
 |    |
 |    O  |  -+-
 |       |
 |
 |
 |
 |
 |
 |
 |
-------
""",
"""
 ------
 |    |
 |    |
 |    O  |  /-+-
 |       |
 |
 |
 |
 |
 |
 |
 |
-------
""",
"""
 ------
 |    |
 |    |
 |    O  |  /-+-/
 |       |
 |
 |
 |
 |
 |
 |
 |
-------
""",
"""
 ------
 |    |
 |    |
 |    O  |  /-+-/
 |    |  |
 |
 |
 |
 |
 |
 |
 |
-------
""",
"""
 ------
 |    |
 |    |
 |    O  |  /-+-/
 |    |  |
 |    |
 |   |
 |   |
 |
 |
 |
 |
-------
""",
"""
 ------
 |    |
 |    |
 |    O  |  /-+-/
 |    |  |
 |    |
 |   | |
 |   | |
 |
 |
 |
 |
-------
""")

max_wrong=len(HANGMAN)-1
try:
    #words=('СЕМЬ','ДЕСЯТЬ','ВОСЕМЬ','ВРЕМЯ','ЧАСЫ','ОДИННАДЦАТЬ','МИНУТА')
    filewords=open("text.txt") #открытие файла списка слов
    words=[]
    for line in filewords:
        line=line.rstrip().upper().split()
        for i in line:
            words.append(i)
#    print (words)
#    input("Stop programm: ")

    word=random.choice(words)
    so_far='*'*len(word)
    #print (so_far, "\n",word)
    wrong=0# количество ошибок
    used=[] #буквы которые игрок отгадал
    print("Добро пожаловать в игру 'Висельница'. Удачи вам!")
    while wrong<max_wrong and so_far !=word:
        print(HANGMAN[wrong])
        print("\nВы уже предлагали следующие буквы",used)
        print("\nСлово состоит из",len(word)-1,"букв")
        print("\nОтгаданное вами слово выглядит сейчас так:\n",so_far)
        guess=input("\n\nВведите букву: ")
        guess=guess.upper()
        while guess in used:
            print("Вы уже предлагали букву", guess)
            guess=input("\n\nВведите букву: ")
            guess=guess.upper()
        used.append(guess)
        if guess in word:
            print("\nДа! Буква",guess,"есть в слове!")
            new=""
            for i in range(len(word)):
                if guess==word[i]:
                    new+=guess
                else:
                    new+=so_far[i]
            so_far=new
        else:
            print("\nК сожалению,буквы",guess,'нет в списке')
            wrong+=1
    if wrong==max_wrong:
        print(HANGMAN[wrong])
        print("\nВас повесили")
    else:
        print("\nВы отгадали!")
    print("\nБыло загадано слово",word)
    input("\nНажмите Enter, чтобы закончить игру")
except(KeyboardInterrupt):
    print("Сделайте правильный выбор и возвращайтесь в игру")
    exit()







