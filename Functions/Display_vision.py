# Without running the code, what do you think will happen here:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three              # No invocation of the function, i.e. no `()` so it
                                # will not output anything

# If we invoke the above function, the output I expect will be:
# 3 / 1 = 3
# 6 / 2 = 3
# 9 / 3 = 3
# 12 / 4 = 3
# ...
# 30 / 10 = 3