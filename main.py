# Import 'random' and 'time' libraries
import random, time


# Store code to exit program in 'exit_program()' (Function)
def exit_program():
    print("\nProgram exiting...")
    for delay in range(5):
        time.sleep(1)


# Generate computer's choice of scissors, paper or stone, and store value in 'computer_choice' (Integer)
computer_choice = random.randint(0, 2)


# Get human's choice and store value in 'human_choice' (String)
while True:
    human_choice = input("\nWhat do you choose? Enter '0' for scissors, '1' for paper or '2' for stone.\n")
    if human_choice == "0" or human_choice == "1" or human_choice == "2":
        break
    else:
        print("\nInvalid input. Only the listed options are available.")


# Compare choices and determine winner. Exit program afterwards
if human_choice == "0" and computer_choice == 0:
    print("\nYou chose scissors.")
    print("\nComputer chose scissors.")
    print("\nIt's a draw.")
    exit_program()
elif human_choice == "1" and computer_choice == 1:
    print("\nYou chose paper.")
    print("\nComputer chose paper.")
    print("\nIt's a draw.")
    exit_program()
elif human_choice == "2" and computer_choice == 2:
    print("\nYou chose stone.")
    print("\nComputer chose stone.")
    print("\nIt's a draw.")
    exit_program()
elif human_choice == "0" and computer_choice == 1:
    print("\nYou chose scissors.")
    print("\nComputer chose paper.")
    print("\nYou win!")
    exit_program()
elif human_choice == "0" and computer_choice == 2:
    print("\nYou chose scissors.")
    print("\nComputer chose stone.")
    print("\nYou lose.")
    exit_program()
elif human_choice == "1" and computer_choice == 0:
    print("\nYou chose paper.")
    print("\nComputer chose scissors.")
    print("\nYou lose.")
    exit_program()
elif human_choice == "1" and computer_choice == 2:
    print("\nYou chose paper.")
    print("\nComputer chose stone.")
    print("\nYou win!")
    exit_program()
elif human_choice == "2" and computer_choice == 0:
    print("\nYou chose stone.")
    print("\nComputer chose scissors.")
    print("\nYou win!")
    exit_program()
elif human_choice == "2" and computer_choice == 1:
    print("\nYou chose stone.")
    print("\nComputer chose paper.")
    print("\nYou lose.")
    exit_program()
