s="htglinh@gmail.com"
a = 0
for i, char in enumerate(s):
    if char == "@":
        if "." in s[i:]:
            a+=1
if a>=1:
    print("OK")
else:
    print("NO")

