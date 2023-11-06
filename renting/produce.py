import os
import pandas as pd
import numpy as np

# Define the folder path
folder_path = "/Users/liushiwen/Desktop/大四上/Bachelor_gown"
def check_column_a(df):
    # Use the str.match method to check the pattern
    pattern = r'^B\d{9}$'
    is_match = df['a'].str.match(pattern)
    
    # Return a Boolean Series indicating which rows match the pattern
    return is_match
df_col = ['student_id', 'name', 'size', 'phone_number']

def add_zero_to_column(df, column_name):
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Convert the specified column to strings and add '0' to the front of each value
    df[column_name] = '0' + df[column_name].astype(str)

    return df

total_df = pd.DataFrame(columns=df_col)
print(total_df)
# Initialize an empty list to store DataFrames
files_with_name = {}
# List all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    # Check if the item is a file
    if os.path.isfile(file_path):
        # You can add more file formats if needed (e.g., '.xlsx', '.json', etc.)
        if filename.endswith('.xlsx'):
            # Read the CSV file into a DataFrame
            df = pd.read_excel(file_path)
            df = add_zero_to_column(df, 'phone_number')
            total_df = pd.concat([total_df,df])



def count_values_in_column(df, column_name):
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Use the value_counts() method to count the occurrences of each value in the column
    counts = df[column_name].value_counts().to_dict()
    
    return counts
def sort_dataframe_by_last_two_numbers(df, column_name):
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Define a custom sorting key function to extract the last two digits from a string
    def last_two_digits(value):
        if isinstance(value, str) and len(value) >= 2:
            return value[-2:]
        return value

    # Sort the DataFrame based on the last two digits in the specified column
    sorted_df = df.sort_values(by=column_name, key=lambda x: x.apply(last_two_digits))

    return sorted_df

total_df = sort_dataframe_by_last_two_numbers(total_df, 'student_id')
total_df = total_df.reset_index(drop=True)
# for ii in range(len(total_df)):
#     print(total_df[['student_id','name']].loc[ii])
print(total_df[['phone_number']].to_string(index=False))
print(count_values_in_column(total_df, 'size'))

            