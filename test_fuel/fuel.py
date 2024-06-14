def convert(fraction):
    while True:
            x, y = map(int, fraction.split("/"))
            try:
                if x > y:
                    fraction = (input("Fraction: "))
                    continue
                else:
                    percentage = round((int(x) / int(y)) * 100)
                    return percentage
            except (ValueError, ZeroDivisionError):
                 continue

def gauge(percentage):
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return str(percentage) + "%"

def main():
    fraction = (input("Fraction: "))
    f = convert(fraction)
    percent = gauge(f)
    print(percent)

if __name__ == "__main__":
    main()
