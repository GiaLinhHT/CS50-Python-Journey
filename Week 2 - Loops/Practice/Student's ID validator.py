# start with 2 letters (department code).
# Followed by 6 digits (ID number).
# No other characters allowed.
def main():
    id = input("ID: ")
    if valid(id):
        print("Valid student's ID")
def valid(s):
    if not (s[0].isalpha() and s[1].isalpha()):
        print("Student's ID must start with two letters representing your department.")
        return False
    a=0
    for i in s:
        if i.isdigit():
            a+=1
    if not (a == 6):
        print("Department code must be followed by 6 digits.")
        return False
    if not s.isalnum():
        print("No other characters allowed.")
        return False
    return True
main()