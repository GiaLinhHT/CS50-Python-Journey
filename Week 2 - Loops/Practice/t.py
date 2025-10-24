s = input("Input a string: ")
for i, char in enumerate(s):
    if s[i].isdigit():
        print("Index:",i+1)
        print("Digit:", char)
        break
else:
    print("No digits found")
