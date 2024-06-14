grocery_list = {}
while True:
    try:
        item = input().strip().lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        print("\n")
        for key in sorted(grocery_list.keys()):
            print(grocery_list[key], key.upper())
        break

