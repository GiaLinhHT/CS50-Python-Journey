groceries = {} #avoid name like "dict", "str","list",...because it is a built-in Python type
while True:
    try: 
        item = input().upper()
    except EOFError:
        break
    else: 
        groceries[item] = groceries.get(item,0)+1
print(groceries)