import json     #This gives pre-built tools to convert Python objects and JSON-formatted text
import statistics   #This gives ready-made functions like max(), min(), mean(), which would be used later in this program

marks = {}  #Creates an empty dictionary. This temporarily holds {name: mark} data in the memory while the program runs.
num_students = int(input("Enter the number of students to be recorded: "))  #Takes an input of the number of students to be recorded. input() by default always returns a string, so int converts it to an actual number to be used in the next line.

for _ in range(num_students):   #Loops for num_students times(number of students you entered in the input statement; previous line number 5). _(underscore) is a naming convention used by Python as a dummy or throwaway variable to signal that the loop variable is purposely not being used.
    #_(underscore) in this context is being used to repeat this specific code block for a fixed number of times. For this specific code, it is the number of students entered as an input iine line number 5.
    name = input("Enter the student's name: ")
    mark = int(input(f"Enter the marks scored by {name}: "))
    #Both name and mark variables are repeated num_student times.
    marks[name]=mark    # after taking input from the above two variable num_studentds times, the values are stored as key-value pair in mark dict.


with open('marks.txt', 'w') as f:   # opens(or creates if it doesn't exist) a txt file with name "marks.txt" in "w"(write) mode
    json.dump(marks, f, indent=2)   # json.dump() takes your Python dict (marks) and serializes it and writes it into file f in one line. indent=2 basically just makes the output look pretty by adding two indentations.

print("Data saved.")


with open('marks.txt', 'r') as f:   # re-opens the same txt file in "r"(read) mode
    data_load = json.load(f)    # json.load() de-serializes the raw text sitting in the file and parses as JSON syntax and loads into the python rpogram.

print("Loaded marks: ", data_load)

def ext_num_val(d):     # ext_num_val is short for "extract numeric values".
    return[v for v in d.values() if isinstance(v, (int, float))]    # d here is a dict. d.values returns only the values of the dict without returning the key of each individual value or simply ignoring the keys of the values.
        # the v before 'for v' in "v for v d.values..." is an expression for what you want to add for each time an iteratiion happens before it lands in the final list. For example: "v*2 for v d.values..." would give double of the real values iterated. If the real output was [82, 102](these are values in dict without their keys) in case of "v for v d.values...", with "v*2 for v d.values...", the final output would be [164, 204].
        # "if isinstance(v, (int, float))" keeps only v's that are integers or floats, filtering out anything else (like strings)
num = ext_num_val(data_load)        #calls the above created function on the reloaded dict on line number 22.
print("Highest mark achieved is: ", max(num))
print("Lowest mark achieved is: ", min(num))
print("Average marks of all the marks is: ", statistics.mean(num))
