class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares = self.shares - nshares

def read_portfolio(filename):
    stocks = []
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            name, shares, price = line.split(',')
            stocks.append(Stock(name.strip(), int(shares), float(price)))
    return stocks

def print_portfolio(stocks: list):
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print("%10s %10s %10s" % ("----------", "----------", "----------"))
    for s in stocks:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))