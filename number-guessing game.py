import random   # random module generates pseudo random numbers 

random_num = random.randint(1, 100)     # generates a random number from 1 to 100. randint generates numbers upto a fixed upper limit unlike range and other similar functions.

print("Welcome to the Number Guessing game Adventurer!")

print("A random number has been generated. Can you guess the number?")


while True:     # an infinite loop which repeats the code block until a given conditional statement is fulfiled: only ends when break rung, which automatically happens when your guess is correct.

    number = int(input("Enter your answer!: "))     # takes input number from the user. int() typing to convert str to int is necessary for the comparision, otherwise a buggy error will be seen.
    
    if number > random_num+10:      # compares the randomly generated number and the input number taken from the user and returns the output if the generated number is 10+ lower.
        print("BEEP BEEP. Too high! Try again.")
        continue     #  Skips the rest of this iteration and jumps back to re-check the loop condition, asking for a new guess. random_num itself doesn't change, since it was only set once, outside the loop.

    elif number > random_num:   # compares the randomly generated number and the input number taken from the user and returns the output if the generated number is slightly lowerr.
        print("BEEP BEEP. Slightly higher than needed. Try again.")
        continue

    elif number < random_num-10:        # compares the randomly generated number and the input number taken from the user and returns the output if the generated number is 10+ higher.
        print("BEEP BEEP. Too low! Try again.")
        continue

    elif number < random_num:       # compares the randomly generated number and the input number taken from the user and returns the output if the generated number is slightly higher.
        print("BEEP BEEP. Slightly lower than needed. Try again.")
        continue

    elif number == random_num:      # If the input answer from the user exactly matches the random number generated this conditional statement is triggerd and you win the game.
        print("DING DING DING!! Correct Answer!")
        print("Congratulations adventurer! You have conquered the game!")

        break    # Breaks from the while loop and exits from the whole program as the condition is triggered.
