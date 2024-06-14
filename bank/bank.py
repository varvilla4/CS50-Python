greet = input("Greeting: ").strip().casefold()

if greet.find("hello") != -1:
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")
