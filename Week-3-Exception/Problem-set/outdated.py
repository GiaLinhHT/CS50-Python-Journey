#input: month-day-year xyz
#output: year-month-day zxy
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        date = date.replace("/"," ")
        x,y,z = date.split()
    except x in month:
        print(f"{z}/{month[month.index(x)+1]}/{y}")
    else:
        if x.isdigit():
            print(f"{z}/{x}/{y}")
        pass


        
    
