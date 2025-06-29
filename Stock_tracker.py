# Predefined stock prices (hardcoded dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "MSFT": 320,
    "AMZN": 140
}
# Dictionary to store user's stock portfolio
portfolio = {}
# Number of different stocks to be added
n = int(input("Enter number of different stocks you own: "))
# Collect stock names and quantities from user
for _ in range(n):
    stock = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    else:
        print(f"Stock symbol '{stock}' not found in predefined list.")
# Calculate total investment
total_value = 0
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    print(f"{stock} - {quantity} shares at ${price} each = ${value}")
    total_value += value
print(f"\nTotal Investment Value: ${total_value}")
# Optional: Save the result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
        for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        file.write(f"{stock} - {quantity} shares at ${price} each = ${value}\n")
    file.write(f"\nTotal Investment Value: ${total_value}\n")
print("Portfolio summary saved to 'portfolio_summary.txt'")
