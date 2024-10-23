def remove_duplicates(customers):
    return list(set(customers))

customer_data = [
    ('Amit Sharma', 'amit.sharma@example.com'),
    ('Bhavna Mehta', 'bhavna.mehta@example.com'),
    ('Amit Sharma', 'amit.sharma@example.com'),
    ('Chirag Patel', 'chirag.patel@example.com'),
    ('Deepa Nair', 'deepa.nair@example.com'),
    ('Bhavna Mehta', 'bhavna.mehta@example.com')
]

unique_customers = remove_duplicates(customer_data)
print(unique_customers)
