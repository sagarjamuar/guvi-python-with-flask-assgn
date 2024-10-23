import re

def extract_phone_numbers(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            pattern = r'(?:\+91-|\+91|0)?\d{10}' 
            return re.findall(pattern, content)
    except FileNotFoundError:
        return "File not found."

filename = 'client_data.txt'
phone_numbers = extract_phone_numbers(filename)
print(phone_numbers)
