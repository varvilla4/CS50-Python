def main():
    time = input("What time is it? ")
    time = (convert(time))
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")


def convert(time):
    y, z = time.split(":")
    time = float(y) + float(z)/60
    return time


if __name__ == "__main__":
    main()
