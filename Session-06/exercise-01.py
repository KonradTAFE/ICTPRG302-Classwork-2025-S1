# Dictionary Exercises
# filename: exercise-01.py
# Write a Python script to concatenate the following dictionaries to create a new one.

dictionary_1 = {1: 10, 2: 20}
dictionary_2 = {3: 30, 4: 40}
dictionary_3 = {5: 50, 6: 60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dictionary_combined = dictionary_1 | dictionary_2 | dictionary_3
print(dictionary_combined)
dictionary = {}

for key, value in dictionary_1.items():
    dictionary[key] = value

for key, value in dictionary_2.items():
    dictionary[key] = value

for key, value in dictionary_3.items():
    dictionary[key] = value

print(dictionary)


