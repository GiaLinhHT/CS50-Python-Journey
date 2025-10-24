#Input: a string.
#Output: index and value of the first digit found.
s = input("Input a string: ")
for i, char in enumerate (s):
    if char.isdigit:
        print(i, s[i])
