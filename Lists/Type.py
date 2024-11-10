some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

print('Some_value1 is a list' if type(some_value1) is list else 'Some_value1 is not a list')
print('Some_value2 is a list' if type(some_value2) is list else 'Some_value2 is not a list')

print(type(some_value1), type(some_value2))

print(isinstance(some_value1, list))
print(isinstance(some_value2, list))