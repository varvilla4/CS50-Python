def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print("\nAdieu, adieu, to ", join_names(names))
            break

def join_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return " and ".join(names)
    else:
        return ", ".join(names[:-1]) + ", and " + names[-1]

if __name__ == "__main__":
    main()







