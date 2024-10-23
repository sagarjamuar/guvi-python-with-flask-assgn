def clean_product_list(product_ids):
    return sorted(set(product_ids))

product_ids = [101, 203, 101, 405, 203, 309, 507, 405, 102, 309]
cleaned_list = clean_product_list(product_ids)
print(cleaned_list)
