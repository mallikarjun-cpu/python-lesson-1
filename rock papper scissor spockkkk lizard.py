import random

comp_c = 0
user_c = 0
x = y = 0

def user_choice():
    print ("Rock-Paper-Scissors game - Choose your thing.")
    user_c = input()
    if user_c in ["rock","r","rok","rocks"]:
        user_c = "rock"
    elif user_c in ["paper","papper","p","paperr"]:
        user_c = "paper"
    elif user_c in ["scissor","scisor","s","scissors","scisor","scissorrs"]:
        user_c = "scissor"
    elif user_c in ["spockk","sp","sd","sk","sa","spok"]:
        user_c = "spk"
    elif user_c in ["lizard","l","lisard"]:
        user_c = "liz"
    else:
        print("did not get that word, type again..")
        user_choice()
    return user_c


def comp_choice():   
    comp_c = random.choice(['rock','paper','scissor','spock','lizard'])
    if comp_c == "lizard":
        comp_c = "liz"
    elif comp_c == "spock":
        comp_c = "spk"
    return comp_c

while True:
    if (x == 5) or (y == 5):       
        break
    else:
        user_i = user_choice()
        print("u have chosen: ", user_i)

        #print(user_choice())

        comp_i = comp_choice()
        print("the computer choose:")
        print(comp_i,"\n")

        if user_i == "rock":
            if comp_i == "scissor":
                print("u win")
                x += 1
            elif comp_i == "paper":
                print("c wins")
                y += 1
            elif comp_c == "spk":
                print("c wins")
                y += 1
            elif comp_i == "liz":
                print("u win")
                x += 1
            else:
                print("draw")
        elif user_i == "scissor":
            if comp_i == "paper":
                print("u win")
                x += 1
            elif comp_i == "rock":
                print("c wins")
                y += 1
            elif comp_c == "spk":
                print("c wins")
                y += 1
            elif comp_i == "liz":
                print("u win")
                x += 1
            else:
                print("draw")
        elif user_i == "paper":
            if comp_i == "rock":
                print("u win")
                x += 1
            elif comp_i == "scissor":
                print("c wins")
                y += 1
            elif comp_i == "spk":
                print("u win:")
                x += 1
            elif comp_i == "liz":
                print("c wins")
                y += 1
            else:
                print("draw")
        elif user_i == "spk":
            if comp_i == "rock":
                print("u win")
                x += 1
            elif comp_i == "paper":
                print("c wins")
                y += 1
            elif comp_i == "scissor":
                print("u win:")
                x += 1
            elif comp_i == "liz":
                print("c wins")
                y += 1
            else:
                print("draw")
        elif user_i == "liz":
            if comp_i == "rock":
                print("c win")
                y += 1
            elif comp_i == "scissor":
                print("c wins")
                y += 1
            elif comp_i == "paper":
                print("u win:")
                x += 1
            elif comp_i == "spk":
                print("u wins")
                x += 1
            else:
                print("draw")

        print(".................SCOREOARD.........................")
        print ("\nyour score is: ",x, "\ncomp score is: ",y,"\n")
        print(".................NEXT ROUND: \n")

if x == 5:
    print("\n....................U ARE A WINNERRR !!!................")
else:
    print("\ncomp has won.................")


 
