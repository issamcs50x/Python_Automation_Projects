import requests

API_KEY = ""

BASE_URL = "https://api.freecurrencyapi.com/v1/latest"


def fetch_currencies(base_currency):
    url = f"{BASE_URL}?apikey={API_KEY}&base_currency={base_currency}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get("data")
            data.pop(base_currency)
            return response.json().get("data")
    except:
        pass
    return {}

def convert(from_, to_, amount):
    data = fetch_currencies(to_)
    if data:
        if from_ in data.keys():
            return round(amount / data.get(from_), 2)
        else:
            print(f"The {from_} currency not available!")
    else:
        print("Somthing wrong occure!")
    return 0

print(convert("EUR", "USD", 2))