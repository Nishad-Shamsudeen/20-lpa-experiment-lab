text = "1xample123"

# Check for at least one capital letter
has_upper = any(char.isupper() for char in text)
print(has_upper)
# Check for at least one numeric digit
has_digit = any(char.isdigit() for char in text)

if has_upper and has_digit:
    print("String contains both a capital letter and a number.")
