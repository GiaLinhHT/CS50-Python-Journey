def get_int():
    while True:
        try:
            x = int(input("x = "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
def main():
    res = get_int()
    print(f"The value of x is {res}")
if __name__ == "__main__":
    main()