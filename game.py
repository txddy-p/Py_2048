import os
import logic


value = None
end_of_game = None

def welcome():
    print(" __          __  _                            _          ___   ___  _  _   ___  ")
    print(" \ \        / / | |                          | |        |__ \ / _ \| || | / _ \ ")
    print("  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___      ) | | | | || || (_) |")
    print("   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    / /| | | |__   _> _ < ")
    print("    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |  / /_| |_| |  | || (_) |")
    print("     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |____|\___/   |_| \___/ ")
    print("by txddy-p")        
                                                                                
def menu():
    global value
    option = input("Select an option:   P - Play Game       Q - Quit\n")
    option = option.upper()
    if option == "P":
        os.system('clear')
        print("Starting a new round!")
        print("Use the wasd keys on the keyboard to make and submit using enter!")
        print("w:Up     a:left      s:down      d:right")
        value = ""
        guess_amount=0
        logic.pb()
        while not end_of_game:
            play()
    elif option == "Q":
        print("Come back soon!")
        exit()
    else:
        print("Invalid option. Please select a valid one!")


def q():
    print("Come back soon!")
    exit()

def play():
    #logic.pb()
    moves = {"W":logic.mup,"A":logic.mleft,"S":logic.mdown,"D":logic.mright,"Q":q}
    value = input("")
    value = value.upper()
    if value in moves:
        moves[value]()
        os.system('clear')
        print(f"You pressed {value}")
        logic.pb()
    
def main():
    pass
    try:
        welcome()
        logic.start()
        while True:
            #logic.pb()
            menu()
            pass
    except Exception as e:
        print(e)
    finally:
        print("Done")

if __name__ == "__main__":
    main()