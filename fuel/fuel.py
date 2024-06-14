def get_percentage():
    while True:
        fraction = (input("Fraction: "))
        try:
            x, y = map(int, fraction.split("/"))
            if x > y:
                continue #return to input 
            percentage = round((int(x) / int(y)) * 100)
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return (f"{percentage}%")
        except (ValueError, ZeroDivisionError):
            pass

def main():
    percentage = get_percentage()
    print(f"{percentage}")

main()




