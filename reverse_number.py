def rev_number(num):

    reversed_number_list = []
    while num > 0:
        last_digit = num % 10
        num = num // 10

        if last_digit == 0 and len(reversed_number_list) == 0:
            continue
        else:
            reversed_number_list.append(str(last_digit))
    reversed_number = ''.join(reversed_number_list)
    return reversed_number

#num = int(input('Enter a positive number: '))
num = int(input('Enter a number: '))
result = rev_number(num)
print(result)