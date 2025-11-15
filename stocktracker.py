# Hardcoded stock prices
STOCK_PRICES = {"AAPL": 180, "TSLA": 250, "GOOG": 135}

# Track investment
total_investment = 0.0

print("Enter your stock holdings. Type 'done' to finish.")
while True:
    ticker = input("Enter stock ticker: ").upper()
    if ticker == 'DONE':
        break

    if ticker in STOCK_PRICES:
        try:
            quantity = int(input(f"Enter quantity of {ticker}: "))
            stock_value = STOCK_PRICES[ticker] * quantity
            total_investment += stock_value
            print(f"Added {quantity} shares of {ticker} for a total of ${stock_value:.2f}")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print(f"Stock ticker '{ticker}' not found.")

# Display total investment
print(f"\nTotal investment value: ${total_investment:.2f}")

# Optional: Save to a text file
with open("portfolio_summary.txt", "w") as f:
    f.write(f"Total Investment: ${total_investment:.2f}\n")
print("Saved summary to portfolio_summary.txt")
