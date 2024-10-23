def currency_conversion(amount, rate):
    try:
        amount = float(amount)
        rate = float(rate)
        if rate == 0:
            return "Conversion rate cannot be zero."
        return amount * rate
    except ValueError:
        return "Invalid input. Please enter numeric values."

amount = input("Enter the amount to convert: ")
rate = input("Enter the conversion rate: ")

result = currency_conversion(amount, rate)
print(result)
