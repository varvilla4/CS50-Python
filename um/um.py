import re


def main():
    print(count(input("Text: ")))


def count(s):
    find_um = re.findall(r"\b([U-u]m)\b", s)
    return len(find_um)

if __name__ == "__main__":
    main()
