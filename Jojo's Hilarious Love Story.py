import time
#objects
dagger = 0
flower = 0
#script printing for choice to eliminate redundancies
rock_line = ("\nThe unknown warrior is stunned, but regains control. He begins " #rock option
                "running towards you again. Will you:")
rock_option = ("""   A. Run \n   B. Throw another rock \n   C. Run towards a nearby abandoned house""")
rock_option_A = ("\nYou decided to throw another rock, as if the first " 
                "rock thrown did much damage. The rock flew well over the "
                "orcs head. You missed. \n\nYou died!")
run_line = ("\nYou run as quickly as possible, but the unknown warrior's "  #run option
            "speed is too great. You will:")
run_option = ("   A. Hide behind boulder\n"
            "   B. You are trapped, so you fight\n"
            "   C. Run towards an abandoned town")
run_option_A = ("You're easily spotted. \n\nYou died!")
run_option_B = ("\nYou're no match against a fully armored warrior. \n\nYou died!")
town_option = ("\nWhile frantically running, you notice a rusted "  #town option
                "dagger lying in the mud. You quickly reach down and grab it, "
                "but miss. You try to calm your heavy breathing as you hide "
                "behind a delapitated building, waiting for the unknown warrior to come "
                "charging around the corner. You notice a perfect red rose "
                "near your foot. Do you pick it up? Y/N")
flower_option = ("You hear its heavy footsteps and ready yourself for "
                "the impending unknown warrior.")
flower_ending = ("\nYou quickly hold out the red rose, somehow "
                "hoping it will stop the unknown warrior. \n ......")
flower_ending1 = ("And It does! The unknown warrior took off the helmet and "
                "found out it's a woman who has been bewitched and cursed but the " 
                "perfect red rose dispelled the curse and delivered her from insanity."
                "The woman is actually the one you sought after and asked her to marry you, "
                "and she accepted you as you were the promised one to save her from the curse."
                "\n\nYou're glad that you didn't kill her and you got married!")
flower_ending2 = ("\nMaybe you should have picked up the red rose. "
                "\n\nYou died!")
house_line = ("\nYou were hesitant, since the abandoned house was dark and "
                "ominous. Before you fully enter, you notice a shiny dagger on "
                "the ground. Do you pick up a dagger. Y/N?")
house_option  = ("""  A. Hide in silence \n  B. Fight \n  C. Run""")
house_option_A = ("\nReally? You're going to hide in the dark? "
                " Not sure, but I'm going with YES, so...\n\nYou died!")
house_option_dagger = ("\nYou laid in wait. The shimmering dagger attracted "
                "the unknown warrior, which thought you were no match. As he walked "
                "closer and closer, your heart beat rapidly. As the unknown warrior "
                "reached out to grab the dagger, you found out there is an opening between "
                "the helmet and the chestplate and you pierced the blade down into "
                "its chest. \n\nYou found out this is a women and the one you sought after, " 
                "you regretted a lot and cried in sorrow that you didn't talked "
                "it out and possibly married her and known her story, nevertheless, "
                "you've survived anyway and hoping to move on in life...")
house_ending = ("\nYou should have picked up that dagger. You're "
                "defenseless. \n\nYou died!")
house_option_C = ("As the unknown warrior enters the dark abandoned house, you sliently "
                "sneak out. You're several feet away, but the unknown warrior turns "
                "around and sees you running.")
required = ("\nChoose A, B, or C only\n") #if user input/answer else
#input of the user
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
play_again = True
while play_again:
    print("You ventured out in a ship to seek learning and find love someday... "
    "You landed to an unkown village with a tavern near the middletown. "
    "You've met some strange people and drank ale with them, you've felt drunk and " 
    "fighting the urge to vomit; as you've spent the night you've fell asleep. "
    "As you've woke up in the next morning, you stand and marvel at your new, "
    "unfamiliar setting. The peace quickly fades when you hear a "
    "grotesque sound emitting behind you. A crazy unknown warrior in a metal "
    "covered-all equipment screaming like a demon is running towards you. You will:")
    time.sleep(1)
    print("""    A. Grab a nearby rock and throw it at the unknown warrior
    B. Lie down and wait to be mauled
    C. Run""")
    option = False #when an option is not yet chosen
    while option == False:
        choice = input(">>> ") #The first choice.
        if choice in answer_A:  #main A
            print(rock_line)
            time.sleep(1)
            print(rock_option)
            choice = input(">>> ")
            
            while option == False:
                if choice in answer_A: #2nd A
                    print(run_line)
                    time.sleep(1)
                    print(run_option)
                    while option == False:
                        choice = input(">>> ")
                        if choice in answer_A:
                            print(run_option_A)
                            option = True
                        elif choice in answer_B:
                            print(run_option_B)
                            option = True
                        elif choice in answer_C:
                            print(town_option)
                            choice = input(">>> ")
                            if choice in yes:
                                flower = 1 #adds a flower
                            else:
                                flower = 0
                            print(flower_option)
                            time.sleep(1)
                            if flower > 0:
                                print(flower_ending)
                                time.sleep(1.5)
                                print(flower_ending1)
                            else: #If the user didn't grab the dagger
                                print(flower_ending2)
                            option = True
                        else:
                            print(required)
                            break
                elif choice in answer_B: #2nd B
                    print(rock_option_A)
                    option = True
                elif choice in answer_C: #2nd C
                    print(house_line)
                    choice = input(">>> ")
                    if choice in yes:
                        dagger = 1 #adds a dagger
                    else:
                        dagger = 0
                    print("\nWhat do you do next?")
                    time.sleep(1)
                    print(house_option)
                    while option == False:
                        choice = input(">>> ")
                        if choice in answer_A: #3rd A
                            print(house_option_A)
                            option = True
                        elif choice in answer_B: #3rd B
                            if dagger > 0:
                                print(house_option_dagger)
                                option = True
                            else: #If the user didn't grab the dagger
                                print(house_ending)
                                option = True
                        elif choice in answer_C: #3rd C
                            print(house_option_C)
                            print(run_line)
                            time.sleep(1)
                            print(run_option)
                            while option == False:
                                choice = input(">>> ")
                                if choice in answer_A:  #4th A
                                    print(run_option_A)
                                    option = True
                                elif choice in answer_B:    #4th B
                                    print(run_option_B)
                                    option = True
                                elif choice in answer_C:    #4th C
                                    print(town_option)
                                    choice = input(">>> ")
                                    if choice in yes:
                                        flower = 1 #adds a flower
                                    else:
                                        flower = 0
                                    print(flower_option)
                                    time.sleep(1)
                                    if flower > 0:
                                        print(flower_ending)
                                        time.sleep(1.5)
                                        print(flower_ending1)
                                        option = True
                                    else: #If the user didn't grab the dagger
                                        print(flower_ending2)
                                        option = True
                                else:
                                    print(required)
                                    break
                        else:
                            print(required)
                            break
                else:
                    print(required)
                    break
                    
        elif choice in answer_B: #main B
            print("\nWoah, that was quick... "
            "\n\nYou died!")
            option = True

        elif choice in answer_C: #main C
            print(run_line)
            time.sleep(1)
            print(run_option)
            while option == False:
                choice = input(">>> ")
                if choice in answer_A:
                    print(run_option_A)
                    option = True
                elif choice in answer_B:
                    print(run_option_B)
                    option = True
                elif choice in answer_C:
                    print(town_option)
                    choice = input(">>> ")
                    if choice in yes:
                        flower = 1 #adds a flower
                    else:
                        flower = 0
                    print(flower_option)
                    time.sleep(1)
                    if flower > 0:
                        print(flower_ending)
                        time.sleep(1.5)
                        print(flower_ending1)
                        option = True
                    else: #If the user didn't grab the dagger
                        print(flower_ending2)
                        option = True
                else:
                    print(required)
                    break
        else:
            print(required)
    time.sleep(1)
    restart = input("\n Would you like to play again? (y/ if not enter any key)\n")
    if restart in yes:
        continue
    else:
        print("Game Over!\n Please exit the game...")
        play_again = False