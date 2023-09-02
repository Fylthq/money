class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        usd_amount = amount * self.exchange_rate
        return usd_amount

exchange_rate = float(input("Введіть курс вашої валюти до долара США: "))

converter = CurrencyConverter(exchange_rate)

amount = float(input("Введіть суму в вашій валюті: "))

usd_amount = converter.convert_to_usd(amount)
print(f"{amount} вашої валюти = {usd_amount} USD")
