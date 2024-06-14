def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
#checking if the length is between 2 and 6 char
    if len(s) < 2 or len(s) > 6:
        return False
    elif not starts_with_letters(s):
        return False
    elif not has_valid_characters(s):
        return False
    elif not_zero(s) == False:
        return False
    else:
        return True

#check if it starts with letters
def starts_with_letters(s):
    return s[:2].isalpha()
#check is it only contains numbers and letters
def has_valid_characters(s):
    return s.isalnum()
#check the first # is not 0
def not_zero(s):
    firstnum = None
    for c in s:
        if c.isdigit():
            firstnum = c
            break
    if firstnum == None:
        return True
    if int(firstnum) == 0:
        return False
    index = s.index(firstnum)
    position = len(s) - index
    for c in s[-position:]:
        if not c.isdigit():
            return False
    return True

if __name__ == "__main__":
    main()
