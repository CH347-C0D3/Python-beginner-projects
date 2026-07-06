print("Greetings player, welcome to the Perbatorium of knowledge.")    # Greetings to the player. 
while True:    # While loop starts here.
    name = input("Before we proceed, please enter your name player: ").strip()    # Takes the name of the player. .strip() function removes the starting or/and ending spaces after the entered name.
    print(f"Very well, player {name}! Answer 5 questions correctly to win.\n")
    
    questions = [        # This is a list of tuples, each one with [question_text, correct_answer] pair
        ("1) Who first described the modern quadratic formula? ", "shridhara"),
        ("2) The more I age, the shorter I become. What am I? ", "candle"),
        ("3) What is the boundary around a black hole called? ", "event horizon"),
        ("4) What is the bone inside your head called? ", "cranium"),
        ("5) Final question: Would you lose? ", "nah, i'd win")
    ]
    
    failed = False    # failed flag starting. This starts with the assumption that player is not wrong until proven wrong.
    for text, answer in questions:    # Here, for loop unpacks each tupple individually, text becomes the question string, answer becomes the correct_answer, one pair per iteration.
        # First attempt
        reply = input(text).strip().casefold()    # Chain reaction of aftereffects on the input since Python in case sensitive. Extended explanation in the incoming multi-line comment.
        if reply != answer:
            # Second attempt
            print("Wrong—try once more.")
            reply = input(text).strip().casefold()
            """
            input(text) gives the string, .strip().casefold() are chained together--input(text) returns a string, 
            .strip() runs on that result, then .casefold() runs on that result. 
            The reason for .casefold() specifically is to make the comparison case-insensitive, since Python's != comparison is case-sensitive by default ("Cranium" != "cranium" would be True without it).
            """
            if reply != answer:
                print("Wrong again! Restarting quiz...\n")
                failed = True     # Here the player is finally proven wrong.
                break    # Exits from the for loop. And restarts from the beginning, because the outer while loop is still active.
        print("Correct!\n")
    
    if not failed:    # If failed = True is not triggered, this block of code gets executed.
        print(f"Congratulations, player {name}! You are now The Archive Monarch!")
        break    # Exits from the while loop completely. And ends the program.
    # else: loop repeats from start, asking name again
