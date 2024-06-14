import emoji

def main():
    str = input("Input: ")
    print("Output: ", emoj(str))

def emoj(em):
    return (emoji.emojize(em))

if __name__ == "__main__":
     main()



