def main():
    email = input("Create your Email account: ")
    if valid(email):
        print("Your Email acount is valid")
def valid(s):
    a = 0
    b = 0
    for i in s:
        if i == " ":
            print("No spaces allowed")
            return False
        if i == "@":
            a+=1
    if a!=1:
        print("Your Email account must contain exactly one @ ")
        return False
    for c,char in enumerate(s):
        if char == "@":
            if "." in s[c:] :
                b+=1
    if not (b>=1):
        print("Your Email account must have at least one '.' after '@'")
        return False
    return True
main()
# Must contain exactly one “@”
# Must have at least one “.” after “@”.
# No spaces allowed