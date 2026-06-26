def main():
    history = []
    while True:
        action = input("Action:")
        if action.lower()=="undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action.lower()=="restart":
            history.clear()
        else:
            history.append(action)
        print(history)
main()