import random

def main():
    n = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(n)
        for i in range(3):
            try:
                answ = int(input(f"{x} + {y} = "))
            except ValueError:
                continue
            else:
                if answ == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {x+y}")
                    continue
    print("Score: ",score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            continue


def generate_integer(level):
    min_value = 10**(level-1)
    max_value = 10**level - 1
    x = random.randint(min_value, max_value)
    y = random.randint(min_value, max_value)
    return x, y

if __name__ == "__main__":
    main()
