try: 
    x = int(input("x = "))
except ValueError: #only run when there occurs value error
    print("x is not an integer")
else: 
    print(f"x is {x}")