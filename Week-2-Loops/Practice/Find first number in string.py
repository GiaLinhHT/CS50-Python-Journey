#Input: a string.
#Output: index and value of the first digit found.
s = input("Input a string: ")
for i, char in enumerate (s):
    if char.isdigit():
        print("Index: ",i+1,"\nDigit: ",char)
        break
else: #lệnh under "else" will only be executed when for loop ends naturally
    print("No digits found.")
    
