with open("Data/portfolio.dat", 'r') as file:
    summ = 0
    for line in file: 
        summ += int(line.split()[1])*float(line.split()[2])
    print(summ)
