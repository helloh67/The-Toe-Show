print("Welcome to The Toe Show! At The Toe Show!, you must name the toe. Name all 5 toes. Each toe is worth 1 point, so get it right to get that point! Will you name every toe correctly? Win to find out!")
Toes = ["Phoe", "Poe", "Bad Moe", "Ringey", "Poey"]
score = 0
for cur in Toes:
    if cur == "Phoe":
        while True:  # Loop for input validation
            questionChoice = input("What is the Big Toe called? Press 1 for the Boe, press 2 for the Phoe, press 3 for the Phoey: ")
            if questionChoice not in ["1", "2", "3"]:
                print("Invalid input! Please choose a number between 1 and 3.")
            else:
                if questionChoice == "2":
                    print("Correct!")
                    score += 1
                else:
                    print("Wrong!")
                break  # Exit the loop after valid input

    elif cur == "Poe":
        while True:
            questionChoice = input("What is the Second Toe called? Press 1 for the Poe, press 2 for the Ioe, press 3 for the Roe: ")
            if questionChoice not in ["1", "2", "3"]:
                print("Invalid input! Please choose a number between 1 and 3.")
            else:
                if questionChoice == "1":
                    print("Yes, queen!")
                    score += 1
                else:
                    print("Wah, wah, wah :,(")
                break

    elif cur == "Bad Moe":
        while True:
            questionChoice = input("What is the Third Toe called? Press 1 for the Moe, press 2 for the Middle Toe, press 3 for the Bad Moe: ")
            if questionChoice not in ["1", "2", "3"]:
                print("Invalid input! Please choose a number between 1 and 3.")
            else:
                if questionChoice == "3":
                    print("Correct-a-moondo!")
                    score += 1
                else:
                    print("Aww man, you are bad at this!")
                break

    elif cur == "Ringey":
        while True:
            questionChoice = input("What is the Fourth Toe called? Press 1 for the Rie, press 2 for The Ringey, press 3 for the Ring Toe: ")
            if questionChoice not in ["1", "2", "3"]:
                print("Invalid input! Please choose a number between 1 and 3.")
            else:
                if questionChoice == "2":
                    print("OMG a A+ for this qu-qu-qu-question!")
                    score += 1
                else:
                    print(":P")
                break

    elif cur == "Poey":
        print("On to the final question! This question has 5 choices instead of 3, muhahaha- *cough* *cough*. Do the question if you dare >:)")
        while True:
            questionChoice = input("Time for the most devastating toe yet! What is the Baby Toe called? Press 1 for the Baby Toe, press 2 for the Poey, press 3 for the Last Toe, press 4 for the Goo Goo Gaa Gaa Toe, press 5 for the Little Toe: ")
            if questionChoice not in ["1", "2", "3", "4", "5"]:
                print("Invalid input! Please choose a number between 1 and 5.")
            else:
                if questionChoice == "2":
                    print("You did it!")
                    score += 1
                else:
                    print("Why?")
    print(f"You got {score}/5 points! Come again for more toe-tastic fun!")