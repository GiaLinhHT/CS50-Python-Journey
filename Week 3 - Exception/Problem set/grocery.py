groceries = {} #avoid name like "dict", "str","list",...because it is a built-in Python type
while True:
    try: 
        item = input().upper()
    except EOFError:
        break
    else: 
        if item in groceries:
            groceries[item] += 1
        else:
            #groceries.update({item:1})
            groceries[item] = 1
for i in sorted(groceries):
    print(f"{groceries[i]} {i}")
