# Debug this code:

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1     # changed `0` to `1`

    for digit in digits:
        product *= digit

    return product

# Taking the LS solution further:

def digit_product(str_num):
    digits = [int(n) for n in str_num]

    product = digits[0]

    for digit in digits[1:len(digits)]:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0
result = digit_product('321')
print(result)  # expect 6
result = digit_product('2737')
print(result)  # expect 294
