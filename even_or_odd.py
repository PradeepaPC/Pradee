def odd_or_even(num):
    if num > 0:
        if num % 2 == 0:
            return f'The number {num} is EVEN'
        else:
            return f'The number {num} is ODD'
    else:
        return 'Enter a number greater than zero'

num = int(input('ENTER A POSITIVE NUMBER:'))
result_num = odd_or_even(num)
print(result_num)