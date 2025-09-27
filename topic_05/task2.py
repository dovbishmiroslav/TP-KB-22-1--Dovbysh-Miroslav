import requests

available_currencies = ["USD", "EUR", "PLN"]

def get_exchange_rate(currency_code):
    
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["rate"]
    return None

def convert_to_uah(amount, currency_code):
   
    rate = get_exchange_rate(currency_code)
    if rate:
        return amount * rate
    else:
        print("Не вдалося отримати курс для", currency_code)

def main():
    print("Доступні валюти для конвертації:", ", ".join(available_currencies))
    currency = input("Введіть код валюти (USD, EUR, PLN): ").upper()

    if currency not in available_currencies:
        print("Неправильна валюта!")
        return

    try:
        amount = float(input("Введіть кількість валюти: "))
    except ValueError:
        print("Помилка: потрібно ввести число.")
        return

    result = convert_to_uah(amount, currency)
    if result is not None:
        print(f"{amount} {currency} = {result:.2f} UAH")

main()
