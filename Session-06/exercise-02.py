# filename: exercise-02.py
# Write a Python script that:

# asks the user to input a number
# when the number is entered, it checks to see if the number is in the dictionary's keys
# if the key is found it outputs "Fount it!" followed by the value for the key

number = input("Enter a number: ")
number = int(number)
value_dictionary = {
    1: "Hello",
    2: "Goodbye",
    3: "Who is this?"
}

if number in value_dictionary.keys():
    print("Found it!", value_dictionary[number])
elif number not in value_dictionary.keys():
    print("Not found.")
