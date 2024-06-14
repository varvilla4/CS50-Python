n1, op, n2 = input("Expression: ").split(" ")
n1 = float(n1)
n2 = float(n2)

if op == "+":
    print(f"{n1 + n2:.1f}")
elif op == "-":
    print(f"{n1 - n2:.1f}")
elif op == "*":
    print(f"{n1 * n2:.1f}")
elif op == "/":
    print(f"{n1 / n2:.1f}")


