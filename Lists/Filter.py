# Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]

# count = 0
# for score in scores:
#     if score >= 100:
#         count += 1

count = len([score for score in scores
         if score >= 100])

# Another students answer:

# count = sum(1 for score in scores if score >= 100)

print(count) # 3
