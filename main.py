from datetime import datetime

class Stock:
    def __init__(self, name, price_history):
        self.name = name
        self.price_history = price_history  # Diccionario con fecha como clave y precio como valor

    def price(self, date):
        return self.price_history.get(date)

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def profit(self, start_date, end_date):
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        start_value = sum(stock.price(start_date_str) for stock in self.stocks if stock.price(start_date_str))
        end_value = sum(stock.price(end_date_str) for stock in self.stocks if stock.price(end_date_str))
        profit = end_value - start_value

        days = (end_date - start_date).days
        
        if days > 0:
            annualized_return = ((end_value / start_value) ** (365 / days)) - 1
        else:
            annualized_return = 0 
        return {'profit': profit, 'annualized_return': annualized_return}
    
# Ejemplo de uso
stock_a = Stock("EmpresaA", {"2022-12-31": 100, "2024-12-31": 150})
stock_b = Stock("EmpresaB", {"2022-12-31": 200, "2024-12-31": 300})

portfolio = Portfolio()
portfolio.add_stock(stock_a)
portfolio.add_stock(stock_b)

start_date = datetime.strptime("2022-12-31", "%Y-%m-%d")
end_date = datetime.strptime("2024-12-31", "%Y-%m-%d")


print(portfolio.profit(start_date, end_date))

