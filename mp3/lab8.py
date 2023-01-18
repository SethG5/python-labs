num = int(input('Enter a number to check: '))
for i in range(2, 21, 2):
    if num % i == 0:
        print(f'{num} is divisible by {i}')
    else:
        print(f'{num} is NOT divisible by {i}')
