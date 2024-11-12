# What errors will this raise, and what do they mean?

def find_first_nonzero_among(numbers): # It looks like this function is expecting a collection to iterate over
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0) # Will raise a Type Error, expecting 1 argument, received 6 positional arguments.
find_first_nonzero_among(1) # Int object is not iterable, type error. Expecting a sequence or other iterable object

# Fixes:

# find_first_nonzero_among([0, 0, 1, 0, 2, 0])
# find_first_nonzero_among([1])