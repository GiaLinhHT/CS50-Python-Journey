try:
    x = int(input("x = "))
except ValueError:
    print("x is not an integer")
print(f"x is {x}")
#in case when input a wrong type of value to x, there will occur NameError, because there is still
#no right type of value has been gán to x variable
