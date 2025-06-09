import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1dt Option
print(random.choice(friends))

# 2nd option
random_index = random.randint(0,4)
print(friends[random_index])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])