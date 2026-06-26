date = "11/10/2007"
date = date.replace("/"," ")
x,y,z = date.split()
if x.isdigit():
    print("True")
else:
    print("False")