while True:
    try:
        fraction = (input("Fraction: "))
        fraction = " ".join(fraction)
        x,z,y = fraction.split()
        x = int(x)
        y = int(y)
        percent = (x/y)*100
    except (ValueError,ZeroDivisionError):
        pass
    else:
        break
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{round(percent,0)}%")