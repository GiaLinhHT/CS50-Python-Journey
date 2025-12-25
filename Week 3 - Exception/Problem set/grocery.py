dict = {}
while True:
    try: 
        item = input().upper()
    except EOFError:
        break
    else: 
        if item in dict:
            dict[item] += 1
        else:
            dict.update({item:1})
for i in sorted(dict):
    print(f"{dict[i]} {i}")
