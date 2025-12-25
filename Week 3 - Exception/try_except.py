try:
    x = int(input("x = "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")