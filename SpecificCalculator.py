import math
def factorial(x):
    return math.factorial(x)

def comb(x, y):
    return math.comb(x, y)

def sqrt(x):
    return math.sqrt(x)

print('Choose what do you want to do.')
print('1 - Factorial')
print('2 - Binomial Coefficient')
print('3 - Square root')

while True:
    choice = input('Enter choice (1, 2 or 3): ')

    if choice in ('1', '3'):
        try:
            num = float(input('Enter the number: '))
        except ValueError:
            print('Invalid. Enter a number.')
            continue
    elif choice in ('2'):
        try:
            num1 = int(input('First number: '))
            num2 = int(input('Second number: '))
        except ValueError:
            print('Invalid. Enter a number.')
            continue

    if choice == '1':
        print('The fatorial of', num, '=', factorial(num))
    
    elif choice == '2':
        print('The binomial coefficient between', num1, 'and', num2, 'is:', comb(num1, num2))

    elif choice == '3':
        print('The', num, 'square root =', sqrt(num))

    
    anothercalculation = input('Need to do another calculation?(Yes/No): ')
    if anothercalculation == "No":
          break
    elif anothercalculation == "no":
          break
    else:
        print("Invalid Input")