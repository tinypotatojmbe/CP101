# String placeholders using .format() method
# Example 1 using {} placeholders
message_1 = "Hi, my name is {}. I live in {} and I love eating {}."
name = input("Enter your name: ")
city = input("Enter the city you live in: ")
food = input("Enter your favorite food: ")
message_1a = message_1.format(name, city, food)
print(message_1a)

# Example 2 using index numbers in .format()
message_2 = "Hi, my name is {0}. I live in {1} and my favorite food is {2}."
name = input("Enter your name: ")
city = input("Enter the city you live in: ")
food = input("Enter your favorite food: ")
message_2a = message_2.format(name, city, food)
print(message_2a)

# String formatting using % operator
movie = "Inception"
rating = 8.8
sampletext_3 = "The movie %s has a rating of %.1f on IMDb." % (movie, rating)
print(sampletext_3)

