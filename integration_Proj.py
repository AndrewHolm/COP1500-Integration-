"""Game"""
__author__ = "Andy Holm"
import time

"""Introduction"""
print("Welcome to the beginning of your journey! ")
time.sleep(3)
print("The year is 1863 and the civil war is in full swing")
time.sleep(3)
print("You need a freind to help along the way!")
friend = input("Who would you like to accompany you in your travels?: ")
time.sleep(3)

def Main():
    print("""
        1. Introduction
        2. Day 1
        3. Help / Info
        4. Exit
        """)

    # Main Menu Title
    ans = input("Where would you like to start? ")
    if ans == "1":
        option_one()
    elif ans == "2":
        day_one()
    elif ans == "3":
        help()
    elif ans == "4":
        exit()
    else:
        print("Invalid Selection Try Again")

def option_one():

    print("\nYou and " + friend + " where on a mission to penetrate the "
            "Confederate defenses near Charlseton South Carolina...")
    time.sleep(5)
    print("Unbeknownst to either of you...")
    time.sleep(2)
    print("The trails you where walking was a common hunting route of a "
            "young Conederate soldier...")
    time.sleep(5)
    print("As night fell you and " + friend + " decided to set up shop and "
            "get some rest...")
    time.sleep(3)
    print("You are awoken to the sound of a dog barking in the distance...")
    time.sleep(3)
    print("You call " + friend + "'s name to see if they hear the dog...")
    time.sleep(3)
    print("There is no response...")
    time.sleep(3)
    print("Once the dog is out of range you climb out of your tent to wake "
            + friend + "...")
    time.sleep(3)
    print("You walk over to find " + friend + "'s tent had been ransacked "
            "and their was no sign of them...")
    time.sleep(3)
    print("You go inside to find nothing but a note that reads...")
    time.sleep(3)
    print('"Bring $50 to the Charlston church within 2 days and ' + friend +
            ' is yours"')
    time.sleep(3)
    print("You try and get some rest to start the journey in the morning...")
    time.sleep(10)
    day_one()


def day_one():
    money = 5
    print("\n\t Day 1\n")

    print( "You wake up at 0600 and immediately take inventory of what you ha"
           "ve...")
    time.sleep(3)
    print("You come up with $5 and enough food to last you the rest "
        "of the 3 days")
    time.sleep(5)
    print("You pack up and ready to head out...\n\t\n Time:  0645\n\n")
    print("To your 'Right' there are footprint "
          "leading down a path, to the 'Left'"
          "you see a building in the distance.")
    time.sleep(3)
    moveOne = input("Which way would you like to go: ")

    if moveOne == "Right":
        print("You walk down the path for a few hours to see where it "
            "leads..\n\t\n Time:  0900\n\n")
        time.sleep(3)
        smallBox = input( "You come upon a small box on the ground.\n Do you "
            "open it? (Y/N):")
        if smallBox == "Y":
            money += 25
            moneyS = str(money)
            print("You found $25!\nYou now have  $" + moneyS)
            time.sleep(3)
        elif smallBox == "N":
            print("What could have been in that box?")

        else:
            input("Not A Valid Selection, press any key to continue ")
            day_one()

        print("you continue down the path until what looks to be a town "
            "comes up on the horizon.")
        time.sleep(3)
        shortCutOne = input(
            "Would you like to 'Continue' into the town or 'Avoid' it "
            "through the forest?: ")
        if shortCutOne == "Continue":
                print("You approach to find out the town is empty")
                print("You enter a building and find 10 dollars "
                      "in a cash register!")
                time.sleep(3)
                money += 10
                moneyS = str(money)
                print("You now have  $" + moneyS + "!")
                time.sleep(3)
                print("its getting dark and you decide that is as far as "
                      "you will go for the day")
                time.sleep(3)
                print("You finished the day with" + moneyS + "'Remember How "
                      "Much You Have'")
                time.sleep(3)
                day_two()

        elif shortCutOne == "Avoid":
                print("You get lost in the forest and starve to death, "
                    + friend + " will never be freed!")
        else:
                input("Not A Valid Selection, press any key to continue ")
                day_one()
    elif moveOne == "Left":
            building = input("you approach the building to find what seems to "
                              "be a trap, do you go 'back' or 'continue'.")
            if building == "back":
                print("you don't remember the way and will never find "
                        + friend + "...")
                day_one()
            elif building == 'continue':
                print("you'r suspicion was correct and you where ambushed")
                day_one()
            else:
                input("Not A Valid Selection, press any key to continue ")
                day_one()
    else:
        input("Not A Valid Selection, press any key to continue ")
        day_one()


def day_two():
    print("\n\t Day 2\n")
    print("\n\t Time:  1200")
    money_input = input("How much money did you have from yesterday?: ")
    money = int(money_input)
    print("Time is running out and only day remains for you to gather the "
        "remaining money and save " + friend + ".")
    time.sleep(3)
    dayTwo = input("While you where asleep someone came into town and left their "
        "horse tied up, do you 'take' it or 'escape' without being seen: ")
    if dayTwo == "take":
        print("They didn't notice you and you manage to ride off")
        time.sleep(3)
        print("once you get far enough away you search the hourse "
            "for what he may have left behind")
        time.sleep(3)
        print("you find 15$ and a map of the town")
        time.sleep(3)
        money += 15
        moneyS = str(money)
        print("You now have $" + moneyS + "!")
        time.sleep(3)
        print("You find the church on the map and set off in that direction.")
        time.sleep(3)
        print("You finished the day with" + moneyS + "'Remember How "
                                                     "Much You Have'")
        time.sleep(3)
        final_ride()

    elif dayTwo == "escape":
        print("While trying to escape out the back you run into the owner "
            "of the horse and are captured.")
        day_one()
    else:
        input("Not A Valid Selection, press any key to continue ")
        day_two()


def final_ride():
    print("\n\t Day 2\n")
    print("two hours have past as you get close to the church \n\t Time:  "
        "1400\n\n")
    time.sleep(3)
    money_input = input("How much money did you have from yesterday? ")
    money = int(money_input)
    time.sleep(3)
    print("you can see people surrounding the church and are timid "
        "as you approach")
    time.sleep(3)
    decision1 = input("Do you want to 'approach' or 'plan' your approach")
    if decision1 == "approach":
        print("they see you coming and are caught off guard")
        time.sleep(3)
        print("you try and explain yourself but they demand you get "
            "off your horse")
        time.sleep(3)
        print("something is wrong, they search you to find you have "
            "stolen one of their horses and owner of the horse was one of"
            " them!")
        time.sleep(3)
        print("It isn't looking good, they take your belongings and "
            "kill you on the spot...")
        time.sleep(3)
        print("looks like " + friend + " will suffer the same fate")
    elif decision1 == "plan":
        print("You circle around and leave the horse in the forest")
        time.sleep(3)
        print("You see " + friend + " tied up in the back of the "
                                  "church and move in")
        time.sleep(3)
        print("You can see a clear path to " + friend + " and have "
              "a decision to make")
        time.sleep(3)
        decision2 = input(
            "Do you try and 'break' him free and 'reveal' yourself")
        if decision2 == 'break':
            print("You make a run for it")
            time.sleep(2)
            print("You make it to " + friend + " and start to cut them loose")
            time.sleep(3)
            print("It's looking promising but at the last minute you are "
                  "spotted")
            time.sleep(3)
            print("you are both captured and will never see the free world"
                  " again!!")
            time.sleep(3)
            day_two()

        elif decision2 == "reveal":
            print("You tell them you have the money")
            time.sleep(2)
            print("they slowly come close and you reach for the money")
            time.sleep(2)
            print("they ask if it is all there")
            time.sleep(2)
            print("through all the chaos you never checked if it was enough")
            time.sleep(2)
            print("you hand it over and they begin to count")
            time.sleep(3)

            if money < 50:
                print("You don't have enough money and are captured along"
                      " with " + friend + ", all that work for nothing...")
                time.sleep(3)
                while money < 50:
                    ans = input("If I let your friend go, will you go back to the "
                          "North? Y/N: ")
                    if ans == "Y":
                        print("You did it!")
                        time.sleep(3)
                        print(friend + "is saved and the journey is over!!")
                        money += 5000
                    else:
                        print("Wrong answer!")
            else:
                print("You did it!")
                time.sleep(3)
                print(friend + "is saved and the journey is over!!")

    else:
        input("Not A Valid Selection, press any key to continue: ")
        day_two()

Main()