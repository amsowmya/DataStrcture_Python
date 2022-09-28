import pandas as pd

# dataset = {
#     'day': ['march 6', 'march 7', 'march 8', 'march 9', 'march 10', 'march 11'],
#     'price': [310, 340, 380, 302, 297, 323]
# }
#
# df = pd.DataFrame(dataset)
# print(df)

stock_price = []
with open('E:\Python\CodeBasics\DataStrcture\stock_price.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_price.append([day, price])

print(stock_price)

# the order complexity is O(n)
for element in stock_price:
    if element[0] == 'Mar-10':
        print(element[1])

print("***********************")

stock_price = {}

with open('E:\Python\CodeBasics\DataStrcture\stock_price.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_price[day] = price

print(stock_price)

# order complexity is O(1)
price = stock_price['Mar-10']
print(price)