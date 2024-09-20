def count_characters(input_string):
    lowercase = 0
    uppercase = 0
    digits = 0
    special_symbols = 0
    
    for char in input_string:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1
    
    return {
        'Lowercase Letters': lowercase,
        'Uppercase Letters': uppercase,
        'Digits': digits,
        'Special Symbols': special_symbols
    }

# Given string
input_string = "18 year old Jolissa loves to eat Anything, Anywhere, and Anytime"
result = count_characters(input_string)

print("Lowercase Letters:", result['Lowercase Letters'])
print("Uppercase Letters:", result['Uppercase Letters'])
print("Digits:", result['Digits'])
print("Special Symbols:", result['Special Symbols'])
