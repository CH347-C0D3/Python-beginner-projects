print("Greetings player, welcome to the Perbatorium of knowledge.")
while True:
    name = input("Before we proceed, please enter your name player: ").strip()
    print(f"Very well, player {name}! Answer 5 questions correctly to win.\n")
    
    questions = [
        ("1) Who first described the modern quadratic formula? ", "shridhara"),
        ("2) The more I age, the shorter I become. What am I? ", "candle"),
        ("3) What is the boundary around a black hole called? ", "event horizon"),
        ("4) What is the bone inside your head called? ", "cranium"),
        ("5) Final question: Would you lose? ", "nah, i'd win")
    ]
    
    failed = False
    for text, answer in questions:
        # First attempt
        reply = input(text).strip().casefold()
        if reply != answer:
            # Second attempt
            print("Wrong—try once more.")
            reply = input(text).strip().casefold()
            if reply != answer:
                print("Wrong again! Restarting quiz...\n")
                failed = True
                break
        print("Correct!\n")
    
    if not failed:
        print(f"Congratulations, player {name}! You are now The Archive Monarch!")
        break
    # else: loop repeats from start, asking name again
