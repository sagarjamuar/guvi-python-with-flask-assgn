import pandas as pd
import os

def analyze_salaries(filename, output_filename):
    if not os.path.isfile(filename):
        print("File not found.")
        return
    try:
        df = pd.read_csv(filename)
        if 'department' not in df.columns or 'salary' not in df.columns:
            print("Invalid data format.")
            return
        result = df.groupby('department')['salary'].agg(['sum', 'mean']).rename(columns={'sum': 'total_salary', 'mean': 'average_salary'})
        result.to_csv(output_filename)
        print("Analysis saved to", output_filename)
    except:
        print("Error processing the file.")

input_filename = 'employee_records.csv'
output_filename = 'salary_analysis.csv'

analyze_salaries(input_filename, output_filename)
