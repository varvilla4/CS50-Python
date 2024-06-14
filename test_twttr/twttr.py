def main():
    str = input("Input: ")
    print(shorten(str))

def shorten(word):
    output = ""
    vowels = ["a","e","i","o","u"]

    for char in word:
        if char.lower() not in vowels:
            output += char
    return output

if __name__ == "__main__":
    main()



