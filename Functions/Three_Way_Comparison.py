# Write a function that compares the length of two strings. 
# It should return -1 if the first string is shorter, 
# 1 if the second string is shorter, and 0 if they're of equal length

def compare_by_length(string1, string2):
    string1_len, string2_len = len(string1), len(string2)

    if string1_len < string2_len:
        return -1
    elif string1_len > string2_len:
        return 1
    else:
        return 0
    
# Another students solution:

# def compare_by_length(string1, string2):
#     diff = len(string1) - len(string2)      # Finds the difference, either pos of neg num
#     return diff and diff // abs(diff)       # Takes advantage of shortcircuiting
#                                             # expression will always eval out to -1, 1 or 0
                                              # If you wanted it to return differnt
                                              # values you would have to refactor the
                                              # code almost entirely...

print(compare_by_length('patience', 'perseverance'))
print(compare_by_length('strength', 'dignity'))
print(compare_by_length('humor', 'grace'))
