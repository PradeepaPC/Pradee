def power(N, R):
    result = pow(N,R) % 1000000007
    return result

number = input('Enter a number:')
reverse = number[::-1]

modulo = power(int(number),int(reverse))
print(modulo)