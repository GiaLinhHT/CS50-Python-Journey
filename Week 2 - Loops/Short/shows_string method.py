SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " spongebob Squarepants",       
    "Phineas and ferb",
    "Kim possible",
    "Jimmy neutron ",
    "the Proud family"
]
 #there are some mistakes when users input data, such as unecessary spaces,wrong capitalize rules
 #
def main():
    for show in SHOWS:
        cleaned_SHOWS=[]
        cleaned_SHOWS.append(show.title().strip())
        print(cleaned_SHOWS)
main()