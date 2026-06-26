menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        item = input("Item: ")
    #except KeyError: - input never raises KeyError
        #pass
    except EOFError:
        break
    else:
        for i in menu: # Time complexity: O(n) per input; unnecessary when dictionaries exist - Dictionaries are made for direct lookup, not looping 
            if i.lower() == item.lower():
                total += menu[i]
print(f"Total: ${total:.2f}")


                        
