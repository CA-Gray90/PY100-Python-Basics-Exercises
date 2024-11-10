# Write a function that counts the number of occurrences of a substring in a string

def count_substrings(s, substring):
    return s.count(substring)

# What if i don't use .count?

def count_substrings(s, substring):
    count = 0
    for char in s:
        if len(s[s.index(char):-1]) >= len(substring):
            if s[s.index(char):len(substring)] == substring:
                count += 1
        else:
            break

    return count

# Another students solution:
# def count_substrings(string, substring):
#     return len(string.split(substring)) - 1


print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0