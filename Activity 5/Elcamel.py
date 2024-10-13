# Prompt the user to input a statement
statement = input("Please type any statement: ")

# Calculate total characters in the statement (including spaces)
total_char_in_the_statement = len(statement)

# Calculate the count of uppercase characters
count_of_upper_case_char = sum(1 for char in statement if char.isupper())

# Calculate the count of lowercase characters
count_of_lower_case_char = sum(1 for char in statement if char.islower())

# Calculate the count of digits
count_of_all_digits = sum(1 for char in statement if char.isdigit())

# Calculate the count of special characters (excluding alphanumeric and spaces)
count_of_special_char = sum(1 for char in statement if not char.isalnum() and not char.isspace())

# Display the results
print(f"Total characters: {total_char_in_the_statement}")
print(f"Uppercase characters: {count_of_upper_case_char}")
print(f"Lowercase characters: {count_of_lower_case_char}")
print(f"Digits: {count_of_all_digits}")
print(f"Special characters: {count_of_special_char}")
