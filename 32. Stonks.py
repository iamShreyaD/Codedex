
# stock prices for each of these weekdays in January 2023
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

# finds the price on a given day x
# here, parameters of days will be in the range of 1 to 20
def price_at(x):
    return stock_prices[x-1]

# finds the maximum price from day a to day b
def max_price(a, b):
    return max(stock_prices[a-1:b])

# finds the minimum price from day a to day b
def min_price(a, b):
    return min(stock_prices[a-1:b])

print(price_at(3))
print(max_price(1, 20))
print(min_price(1, 20))