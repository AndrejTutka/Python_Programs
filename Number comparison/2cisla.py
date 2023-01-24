try:

    a = int(input('enter a number:  '))
    b = int(input('enter a another number:  '))


    if a > b:
        print(f'greater number is {a}')
    elif b > a:
        print(f'greater number is {b}')
    elif a == b:
        print('they are the same number')

except ValueError:
        print('Both numbers are not intigers')