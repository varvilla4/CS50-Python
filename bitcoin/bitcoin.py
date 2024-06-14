import requests
import sys

def getting_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit()

def main():
    try:
        bitcoins_number = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = getting_price()
    print(f"${bitcoins_number * price:,.4f}")

if __name__ == "__main__":
    main()

