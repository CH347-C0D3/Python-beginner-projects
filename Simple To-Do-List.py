pending = {}    # Empty dictionary for storing tsks in the future.


while True:     # Infinite loop with no built-in stop condition — only ends when a break is reached somewhere inside
    
    print("Welcome to the Python to_do_list.")
    choice = input("""
    1. Add Tasks
    2. End the program
    Choose an option: """)

    if choice == "1": 
        number_task = int(input("Please enter the number of tasks you desire to complete:"))


        for i in range(number_task):    # Repeats the loop number_task times.
            tasks = input(f"Please enter task number {i+1}: ")      # The i iterates from 0 upto(but not including) number_task. The resultant output starts from 1 and so forth. 
            pending[i] = tasks      # After taking input from the above variable number_task times, the values are stored as key-value pair in pending.

        print("1.Tasks Pending:")

        for key, value in pending.items():
            print(key, value)

        choose = input("Press 2 to quit program: ")
        
        if choose == "2":   # This conditional break and ending the program works only when the initial "if" statement is triggered and reaches until this point, and exits from the whole while loop, ending the infinite loop.
                break

    elif choice == "2":     # Only runs if choice isn't "1" AND choice is exactly "2"; any other input (e.g. "3", blank, typo) skips both branches and just loops back to the menu
        break
