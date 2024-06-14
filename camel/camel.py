camelcase = input("camelCase: ")
print("snake_case: ", end="")

for c in camelcase:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")
print("")
