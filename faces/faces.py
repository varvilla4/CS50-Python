def main():
    str = input("write any input: ")
    print(convert(str))

def convert(str):
    return str.replace(":)","🙂").replace(":(","🙁")

main()
