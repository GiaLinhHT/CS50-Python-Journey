#Input: a string.
#Output: number of letters, digits, and special characters.
s = input("Input a string: ")
a = 0 
b = 0
c = 0
for i, char in enumerate(s):
    if char.isalpha():
        a+=1
    elif char.isdigit():
        b+=1
    else:
        c+=1
print("Number of letters are:",a)
print("Number of digits are:",b)
print("Number of special characters are:",c)