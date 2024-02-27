def convert_to_indian_currency(n):
    # Convert the number to string for manipulation
    s = str(n)

    # If the number is less than 1000, no comma is needed
    if len(s) <= 3:
        return s

    # Start with the rightmost three digits
    result = s[-3:]

    # Then add a comma and the next two digits iteratively
    for i in range(3, len(s), 2):
        segment = s[-(i+2):-i] if i+2 < len(s) else s[0:len(s)-i]
        result = segment + "," + result if segment else result

    return result


# Test the function
input_value = 504678
formatted_currency = convert_to_indian_currency(input_value)
print(formatted_currency)
