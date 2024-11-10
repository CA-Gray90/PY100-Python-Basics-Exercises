# Write a function that checks whether a string starts with a specific prefix

def starts_with(s, prefix):
    return s.startswith(prefix)

# If I can't use .startswith()

# def starts_with(s, prefix):
#     return s[:len(prefix)] == prefix

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True