def last_digit(num):
    if num == 0:
        print('The last digit is 0')
    elif num < 0:
        abs_num = abs(num)
        remainder = abs_num % 10
        print(f'THE LAST DIGIT IN {num} is {remainder}')
    else:
        remainder = num % 10
        print(f'THE LAST DIGIT IN {num} is {remainder}')

num = int(input('Enter a number: '))
last_digit(num)