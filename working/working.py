import re
import sys


def main():
    print(convert(input("Hours: ")))



def convert(s):
    if matches := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)$",s):
        if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
            raise ValueError

        first = create(int(matches.group(1)), matches.group(2), matches.group(3))
        second = create(int(matches.group(4)), matches.group(5), matches.group(6))
        return first + " to " + second

    else:
        raise ValueError

def create(hour,minute,time):
    if time == "PM":
        if hour == 12:
            hour = 12
        else:
            hour += 12
    else:
        if hour == 12:
            hour = 0

    if minute == None:
        minute = ":00"
        result = f"{hour:02}{minute:02}"

    else:
        result = f"{hour:02}:{minute:02}"

    return result

if __name__ == "__main__":
    main()
