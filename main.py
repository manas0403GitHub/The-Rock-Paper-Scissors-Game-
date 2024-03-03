
import random
import os, time

i = "" # i is used for alignment
againY = "Yes" # It's used for score saving
AIScore = 0 # For Player 2 Score
YourScore = 0 # Your Score
Points = 0 # Points
PowerUps = [] # PowerUps Have
Settings = "N"

while True:
    # Title:
    if againY == 'No' or againY == 'Yes':
        print("")
        print(f"{i: ^70} The Rock, Paper, Scrissors Game!")
        print("")
        menu = input("""◀️  S to Start, 
        ❌ Q to quit, 
        👍 P to PowerUps
        🔄 SS to Settings: """)
        os.system('cls' if os.name == 'nt' else 'clear')

    if menu == 'S':
        AIScore = 0
        YourScore = 0
        if againY == 'Yes':
            def main_elements():
                AiChoose = random.randint(1, 3)
                # MAIN Elements:
                    # Choose:
                print("""What do you want to choose?
                    🪨 (Rock), 🧻(Paper), ✂️ (Scissors)""")
                # Chooses
                if 'CHEAT PAPER' in PowerUps:
                    choose = input("Choose as R(Rock) P(Paper) S(Scissors) CP(Cheat Paper)< ")
                elif 'PLAYER 2 SCORE' in PowerUps:
                    choose = input("Choose as R(Rock) P(Paper) S(Scissors) P2S(Player 2 Score)< ")
                elif 'INVINCIBE' in PowerUps:
                    choose = input("Choose as R(Rock) P(Paper) S(Scissors) IN(Invincibe)< ")
                else:
                    choose = input("Choose as R(Rock) P(Paper) S(Scissors)< ")
                global AIScore   
                global YourScore

                time.sleep(0.5)
                if choose == 'CP':
                    print("Rock Paper Scissors Cheat!")
                    
                elif choose == 'P2S':
                    print("Rock Paper Scissors -1!")
                else:
                    print("Rock Paper Scissors Shoot!")
                print("")

                time.sleep(0.3)
                if choose == 'CP':
                    print(AiChoose)
                    print("1 = Rock, 2 = Paper, 3 = Scissors")
                    choose = input("Choose as R(Rock) P(Paper) S(Scissors)< ")
                    time.sleep(0.5)
                    print("Rock Paper Scissors Shoot!")
                    PowerUps.remove("CHEAT PAPER")
                    print("")

                elif choose == 'P2S':
                    AIScore -= 1
                    PowerUps.remove("PLAYER 2 SCORE")

                if choose == 'IN':
                    time.sleep(0.5)
                    print("Rock Paper Scissors Shoot!")
                    print("")

                    print("Invincibe!")
                    print("")
                    print(f"Your Score: {YourScore}")
                    print(f"Player 2 Score: {AIScore}")
                    PowerUps.remove("INVINCIBE")

                if choose == 'R' and AiChoose == 2:
                    print("Player 2's Paper Smoothered Your's Rock!")
                    AIScore += 1
                    if Settings == 'H' or Settings == 'HH':
                        AITrick = random.randint(1, 2)
                        if AITrick == 1:
                            AiChoose == 1

                elif choose == 'P' and AiChoose == 1:
                    print("Your Paper Smoothered Player 2's Rock!")
                    YourScore += 1
                    Points += 1
                    if Settings == 'N':
                        AIRevenge = random.randint(1, 2)
                        if AIRevenge == 1:
                            AiChoose == 2

                elif choose == 'P' and AiChoose == 3:
                    print("Player 2's Scissors Cuts Your's Paper!")
                    AIScore += 1
                    if Settings == 'H' or Settings == 'HH':
                        AITrick = random.randint(1, 2)
                        if AITrick == 1:
                            AiChoose == 1

                elif choose == 'S' and AiChoose == 2:
                    print("Your Scissors Cuts Player 2's Paper!")
                    YourScore += 1
                    Points += 1
                    if Settings == 'N':
                        AIRevenge = random.randint(1, 2)
                        if AIRevenge == 1:
                            AiChoose == 2

                elif choose == 'S' and AiChoose == 1:
                    print("Player 2's Rock Breaks Your's Scissors!")
                    AIScore += 1
                    if Settings == 'H' or Settings == 'HH':
                        AITrick = random.randint(1, 2)
                        if AITrick == 1:
                            AiChoose == 1

                elif choose == 'R' and AiChoose == 3:
                    print("Your Rock Breaks Player 2's Scissors!")
                    YourScore += 1
                    Points += 1
                    if Settings == 'N':
                        AIRevenge = random.randint(1, 2)
                        if AIRevenge == 1:
                            AiChoose == 2
                else:
                    print("Is a Tie!")
                print("")

                print(f"Your Score: {YourScore}")
                print(f"Player 2 Score: {AIScore}")
                
        def main_system():
                main_elements()
                # Again
                again = input("Again? Y/N: ")
                if again == 'Y':
                    againY = "Yes"
                    os.system('cls' if os.name == 'nt' else 'clear')
                    YourScore == 0
                    AIScore == 0
                    main_elements()
                    continue

                elif again == 'N':
                    # When the var again equals to 'N'
                    againY = "No"
                    exit()
                else:
                    print("Use Upper Case")

        main_system()
    elif menu == 'Q':
        exit()# Exits the Game

    elif menu == 'SS':
        print(f"Current:-{Settings}")
        Settings = input("""Settings:-
              Difficulty-
              Easy:
                         In Easy mode, Player 2 is not smart or revenge.
              Normal:
                         In Normal mode, Player 2 is not smart but, its does revenge.
              Hard:
                         In Hard mode, Player 2 is smart and revenge.
              Hard+:
                         In Hard+ mode, Player 2 is the same as Hard mode but you dont have any powerups.
                         
              Which do you want to choose?
                         E(Easy) N(Normal) H(Hard) HH(Hard+): """)
        
        if Settings == 'E':
            print("Set! to Easy")

            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif Settings == 'N':
            print("Set! to Normal")

            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif Settings == 'H':
            print("Set! to Hard")

            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif Settings == 'HH':
            print("Set! to Hard+")

            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            print("Pls you Uppe case or enter a different one")
            print("Back to Start menu")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    elif menu == 'P':
                if Settings != 'HH':
                    agained = 'No'
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Points)
                    if Settings == 'H':
                        print("""PowerUps:-
                            1: 📰 Cheat Paper - The Cheat Paper helps to find what the other Player Move. Cost:- 15
                            2: 👍Boost Score - The Boost Score add a extra Point. Cost:- 18
                            3: 💯 Player2 Score - The Player2 Score -1 Point to Player 2. Cost:- 30
                            4: 🤞Invincible - The Invincible can make you win. Cost:- 50""")
                        
                    elif Settings == 'E':
                        print("""PowerUps:-
                            1: 📰 Cheat Paper - The Cheat Paper helps to find what the other Player Move. Cost:- 3
                            2: 👍Boost Score - The Boost Score add a extra Point. Cost:- 6
                            3: 💯 Player2 Score - The Player2 Score -1 Point to Player 2. Cost:- 10
                            4: 🤞Invincible - The Invincible can make you win. Cost:- 13""")
                        
                    elif Settings == 'N':
                        print("""PowerUps:-
                            1: 📰 Cheat Paper - The Cheat Paper helps to find what the other Player Move. Cost:- 10
                            2: 👍Boost Score - The Boost Score add a extra Point. Cost:- 8
                            3: 💯 Player2 Score - The Player2 Score -1 Point to Player 2. Cost:- 15
                            4: 🤞Invincible - The Invincible can make you win. Cost:- 30""")
                        
                    buy = input(""""Do you want to buy CP(Cheat Paper),
                                BS(Boost Score), P2S(Player 2 Score) or IN(Invincibe) N(Exit)?""")
                        
                    if buy == "CP": # Cheat Paper
                        if Points >= 10 and Settings == 'N' or Points >= 15 and Settings == 'H' or Points >= 3 and Settings == 'E':
                            print("You have buyed The Cheat Paper")
                            print("In game, Enter CP to access the Cheat Paper")
                            print("")
                            print(f"{i: ^70} The Rock, Paper, Scrissors Game!")
                            print("")
                            PowerUps.append("CHEAT PAPER")
                            Points -= 5
                            Amount = PowerUps.count("CHEAT PAPER")
                            print(f"you have {Amount} of Cheat Papers")
                            continue
                        else:
                            print("Sorry you don't have the Points")
                            continue

                    elif buy == "BS": # Boost Score
                        if Points >= 8 and Settings == 'N' or Points >= 18 and Settings == 'H' or Points >= 6 and Settings == 'E':
                            print("You have buyed the Boost Score")
                            print("Point added")
                            print(Points)
                            Points += 1
                            continue
                        else:
                            print("Sorry you don't have the Points")
                            continue

                    elif buy == "P2S": # Player 2 Score
                        if Points >= 15 and Settings == 'N' or Points >= 30 and Settings == 'H' or Points >= 10 and Settings == 'E':
                            print("You have buyed the Player 2 Score")
                            print("In game, Enter P2S to access the Player 2 Score")
                            print("")
                            PowerUps.append("PLAYER 2 SCORE")
                            Amount = PowerUps.count("PLAYER 2 SCORE")
                            print(f"you have {Amount} of Player 2 Score")
                            Points -= 20
                            continue
                        else:
                            print("Sorry you don't have the Points")
                            continue

                    elif buy == "IN": # Invincibe
                        if Points >= 30 and Settings == 'N' or Points >= 50 and Settings == 'H' or Points >= 13 and Settings == 'E':
                            print("You have buyed the Invicibe")
                            print("In game, Enter IN to access the Player Invincibe")
                            print("")
                            PowerUps.append("INVINCIBE")
                            Amount = PowerUps.count("INVINCIBE")
                            print(f"you have {Amount} of Invincibe")
                            Points -= 50
                            continue
                        else:
                            print("Sorry you don't have the Points")
                            continue
                else:
                    print("You are in Hard+, so the Powerups are not available.")
                    continue
