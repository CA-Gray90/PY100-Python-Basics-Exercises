# Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.

import random
random_number = random.randint(0, 1)

print(random_number)
if random_number == 0:
    print('No.')
else:
    print('Yes!')

# Refactored to remove the '==' equality check:

# if random_number:
#     print('No.')
# else:
#     print('Yes!')

# Refactored as a Ternary expression:

print('Yes!' if random_number else 'No.')
