def main():
    greet = input("Greeting: ").strip().lower()
    print(f"${value(greet)}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.find("hello") != -1:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
