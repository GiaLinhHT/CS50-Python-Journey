def get_int():
    while True:
        try:
            return int(input("x = "))
        except ValueError:
           pass
def main():
    res = get_int()
    print(f"The value of x is {res}")
if __name__ == "__main__":
    main()
# 'pass' is used to help ignore the error existing, just continue to ask for the right value again and again until the program gets the right one