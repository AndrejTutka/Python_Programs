try:

    a = input('enter a number:  ')
    b = input('enter a another number:  ')


    if a > b:
        print(f'greater number is {a}')
    if b > a:
        print(f'greater number is {b}')
    if a ==b:
        print('they are the same number')

except ValueError:
        print('Both numbers are not intigers')