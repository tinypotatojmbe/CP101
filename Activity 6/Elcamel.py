# Create a Python code that solves the following exercises by applying the appropriate string formatting

# Part 1: Basic f-string Formatting
# Prompt the user for input.
city = input("What is your city? ")
hobby = input("What is your favorite hobby? ")
dream_job = input("What is your dream job? ")

# Using an f-string to format the output
print(f"Hello! I live in {city}, I enjoy {hobby}, and my dream job is to be a {dream_job}.")

# Part 2: Using .format()
# Prompt the user for input.
movie_title = input("What is your favorite movie? ")
book_title = input("What is your favorite book? ")

# Using .format()
message = "My favorite movie is {} and my favorite book is {}.".format(movie_title, book_title)
print(message)

# Part 3: Legacy % formatting.
continent = "Asia"
population_millions = 4.6
area_sq_km = 447.4

# Using % operator
print("The continent of %s has a population of %.1f million and an area of %.1f square kilometers." % (continent, population_millions, area_sq_km))
