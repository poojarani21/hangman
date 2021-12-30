import random 
def hangman():
    list_of_word=["puja","barsa","sradhanjali","subhadra","bably","swarnalata","abhipsa","jyotrmayee","gulnaaz","trupti","shushree"]
    word=random.choice(list_of_word)
    turns=10
    guessmade=" "
    valid_entry=set('abcdefghijklmnopqrestuvwxyz')
    while len(word)>0:
        main_word=" "
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("..you won..")
            break
        print("guess the word",main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid char...")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left")
                print("    O        ")
            if turns==8:
                print("8 turns left")
                print("    O       ")
                print("    |       ")
            if turns==7:
                print("7 turns left")
                print("     O       ")
                print("    \|/      ")
            if turns==6:
                print("6 turns left")
                print("     O       ")
                print("    \|/      ")
                print("     |       ")
            if turns==5:
                print("5 turns left")
                print("     O       ")
                print("    \|/      ")
                print("     |       ")
                print("    / \      ")
            if turns==4:
                print("4 turns left")
                print("     |       ")
                print("     O       ")
                print("    \|/      ")
                print("     |       ")
                print("    / \      ")
            if turns==3:
                print("3 turns left")
                print("     ______       ")
                print("          |       ")
                print("          O       ")
                print("         \|/      ")
                print("          |       ")
                print("         / \      ")
            if turns==2:
                print("2 turns left")
                print("   ______     ")
                print("  |      |    ")
                print("  |      o    ")
                print("  |     \|/   ")
                print("  |      |    ")
                print("  |     / \   ")
                print("  |           ")
            if turns==1:
                print("you have only 1 chance ")
                print("   ______     ")
                print("  |      |    ")
                print("  |      o    ")
                print("  |     \|/   ")
                print("  |      |    ")
                print("  |     / \   ")
                print("  |           ")
                print(" -------------------")
            if turns==0:
                print("....oppppsssssss...")
                print("** you loose **")
                print("your word is",word)
                print("<<<<      >>>>")
                print("   ______     ")
                print("  |      |    ")
                print("  |      o    ")
                print("  |     \|/   ")
                print("  |      |    ")
                print("  |     / \   ")
                print("  |           ")
                print(" -------------------")
                break
name=input("enter your name - ")
print("welcome",name,".....") 
print(".......................") 
print("try to guess the word in less than 10 attempt") 
hangman()         


                
                
                


                