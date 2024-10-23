import pandas as pd
import os

def filter_low_stock_products(filename):
    if not os.path.isfile(filename):
        print("File not found.")
        return
    try:
        df = pd.read_csv(filename)
        if 'product_id' not in df.columns or 'name' not in df.columns or 'quantity' not in df.columns:
            print("Invalid data format.")
            return
        low_stock_products = df[df['quantity'] < 10]
        print("Products with low stock:")
        print(low_stock_products)
    except:
        print("Error processing the file.")

filename = 'product_inventory.csv'
filter_low_stock_products(filename)
