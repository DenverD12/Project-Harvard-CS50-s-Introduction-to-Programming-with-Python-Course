
x = input("What is x? ")
y = input("What is y? ")

# int() converts input which is always a string to INTEGER
# NOTE: can also have int() around the input itself but it is easier to debug if not
# result = int(x) + int(y)
# print(result)

# float() converts input which is always a string to FLOAT, i.e. DECIMAL
result_2 = float(x) + float(y)
print(f"Float Answer = {result_2}")

# rounding numbers -> round(number[, ndigits])
result_rounded = round(result_2)
print(f"Rounded Answer = {result_rounded}")

# rounding numbers to n digits e.g. to 2 decimal places
result_rounded_2dig = round(result_2, 2)
print(f"Rounded to 2 Digits = {result_rounded_2dig}")

# exact same thing using fstring method to 2 decimal places
print(f"Rounded to 2 Digits V2 = {result_2:.2f}")

# printing out numbers with COMMAS at every 1000
print(f"Rounded Result with Comma Separation {result_rounded: ,}")

