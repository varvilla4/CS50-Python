from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    x = input("Date of Birth: ")
    print(diff_to_words(x))

def diff_to_words(x):
    if "-" in x:
        year, month, day = x.split("-")
        x = date(int(year), int(month), int(day))
    else:
        sys.exit("Invalid date")
    difference =  (date.today() - x).days * 24 * 60
    result = p.number_to_words(difference, andword="").capitalize()
    return result + " minutes"


if __name__ == "__main__":
    main()
