def portfolio_cost(filename):

    with open(filename, 'r') as file:
        summ = 0
        for line in file:
            try:
                quantity = int(line.split()[1])
                share_price = float(line.split()[2])
                summ += quantity*share_price
            except (ValueError, TypeError) as e:
                print(f"Couldn't parse line: {line}")
                print(e)
            
    return summ

print(portfolio_cost('Data/portfolio.dat'))
print(portfolio_cost('Data/portfolio3.dat'))