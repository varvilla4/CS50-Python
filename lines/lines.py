import sys

if len(sys.argv) == 2:
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
        total_lines = 0

        for line in lines:
            if not line.lstrip().startswith("#") and line.lstrip() != "":
                total_lines = total_lines + 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(total_lines)


elif len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) <= 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].rsplit(".")[1] != "py":
    sys.exit("Not a Python file")

