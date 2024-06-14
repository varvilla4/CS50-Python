import random
def main():
    n = level()
    g = guess(n)

def level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 :
                return level
        except ValueError:
            pass

def guess(level):
    r = random.randint(1,level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < r:
                print("Too small!")
            elif guess > r:
                print("Too large!")
            else:
                print("Just right!")
                return
        except:
            pass

main()





