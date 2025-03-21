tic_tac = "- X O\n" + "X - X\n" + "O - O\n"

# - X O\nX - X\nO - O\n
#            11 111111
# 012345 678901 234567

# code to print the length of a string
print(len(tic_tac))

# print a specified character
print(tic_tac[12])

# print only first 5 characters
print(tic_tac[0:5])

# print characters 8 to 10
print(tic_tac[7:10])

# print every other character
print(tic_tac[0:18:2])
print(tic_tac[::2])

# various others
print(tic_tac.lower())
print(tic_tac.upper())
print(tic_tac.title())
print(tic_tac[0:5].center(50))
print(tic_tac.capitalize())
print(tic_tac.replace('O', 'P'))
