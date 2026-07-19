import random

questions = {"Apple":"Fruit",
             "Potato":"Vegetable",
             "Orange":"Fruit",
             "Clove":"Spice"
             }

random_key = list(questions.keys())     # Turns the keys of the dictionary into a list as a dict cannot be directly made randomly shuffled.


print("""Welcome to Python Flashcard competition! Fret not! The questions are very easy!.
    You just need to answer whether the question is a fruit, vegetable or something else!""")

for i in range(1, 5):
    

    random_q = random.choice(random_key)
    random_key.remove(random_q)         # Pick a random question and immediately remove it so it can't be picked again.
    
    user_answer = input(f"{i}. What category is {random_q}? Your answer: ").strip().casefold()      # Ask the user the question, inserting the current loop number (i)
    
    if user_answer == questions[random_q].casefold():       #  Check the answer
        print("Correct answer!\n")
    else:
        print(f"Wrong answer! The correct answer was {questions[random_q]}. Game Over!")
        exit()       # This stops the entire program right here

print("Congratulations! You have won the game!")
