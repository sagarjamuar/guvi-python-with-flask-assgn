def organize_sales_data(sales):
    sales_dict = {}
    for name, amount in sales:
        sales_dict[name] = sales_dict.get(name, 0) + amount
    return dict(sorted(sales_dict.items()))

sales_data = [('Alice', 200), ('Bob', 150), ('Alice', 300), ('Charlie', 400), ('Bob', 100)]
organized_sales = organize_sales_data(sales_data)
print(organized_sales)
