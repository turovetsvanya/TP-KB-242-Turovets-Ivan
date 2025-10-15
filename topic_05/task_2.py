import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
data = response.json()

rates = {}
for item in data:
    if item["cc"] in ["USD", "EUR", "PLN"]:
        rates[item["cc"]] = item["rate"]

print("Exchange rates (UAH per 1 unit):")
for code, rate in rates.items():
    print(f"{code}: {rate} UAH")

currency = input("Enter currency (USD, EUR, PLN): ").upper()
amount = float(input("Enter amount: "))

if currency in rates:
    result = amount * rates[currency]
    print(f"{amount} {currency} = {result:.2f} UAH")
else:
    print("Unsupported currency.")