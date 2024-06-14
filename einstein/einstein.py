def main():
    m = int(input("What's the mass?: "))
    print(energy(m))

def energy(m):
    c = pow(300000000, 2)
    E = m*c
    return E

main()
