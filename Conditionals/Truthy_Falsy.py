# Recall all Falsy values in Python:
# Empty collections, strings, False, 0, 0.0, complex 0, None, range(0)

falsy_list = [False, [], {}, (), range(0), '', 0, 0.0, None]
for item in falsy_list:
    print(bool(item))

# from the documentation:
# Constants defined as False: False and None
# Empty Collections and Sequences: [], {}, (), set(), '', range(0), these return a len() of zero
# zero of any numeric type
