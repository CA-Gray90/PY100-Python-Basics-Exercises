# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game.
# However, we encountered an issue, as whenever we change a value in one nested
# list, all nested lists are affected. Can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

# for _ in range(3):
#     matrix.append(sub_list)   # Here we add the same object that sub_list references 3 times. Therefore each element in matrix will point to the same object

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']] # The problem is each element in matrix references the same object that sub_list references.

# for _ in range(3):
#     matrix.append(list(sub_list))   # We use the list constructor function to create a new list object each time we append it to matrix

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# LS solution:

# for _ in range(3):
#     matrix.append(sub_list.copy())  # copy method creates a shallow copy.

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

for _ in range(3):
    matrix.append(sub_list[:])  # [:] uses index slicing to return a copy of the list, a pythonic solution

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]