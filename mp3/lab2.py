cost = float(input('Cost: '))
if cost < 100:
    print(f'No tax charge.\nYour new total is {cost}')
else:
    newCost = cost + (cost * 0.05)
    print(f'You will be charged 5% tax\nYour new total is {newCost}')
