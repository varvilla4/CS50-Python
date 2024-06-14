import validators

def main():
    print(validation(input("What's your email address? ")))

def validation(s):
    if validators.email(s):
        return "Valid"
    else:
        return "invalid"

if __name__ == "__main__":
    main()
