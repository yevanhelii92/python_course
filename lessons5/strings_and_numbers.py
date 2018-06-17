def number_and_strings(string, letter_or_number):
    n = 0
    for i in string:
        if i.lower() == letter_or_number.lower():
             n += 1
    return n

print(number_and_strings('Hello worl12','1'))
