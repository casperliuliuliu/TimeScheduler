import os
import pandas as pd
import numpy as np


# Define a function to validate each value
def validate_value(value):
    if value in [0, 1] and isinstance(value, int):
        return True
    return False

# Define the folder path
folder_path = "/Users/liushiwen/Desktop/大四上/schedule"

# # Initialize an empty list to store DataFrames
columns_name = ['mon', 'tue', 'wed', 'thu', 'fri']
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
            is_valid = df.applymap(validate_value)

            if is_valid.all().all():
                array = df.to_numpy()
                files_with_name[filename] = array
                # print("All values in the DataFrames are valid (belong to {0, 1} and are integers).")
            else:
                print(f"There are invalid values in the DataFrames of [{filename}]")
left = list(files_with_name.keys())
def special(str):
    return int(str[8:10])
left = sorted(left, key=special)
print(f"Total people: {len(left)}")
for name in left:
    print(name)
print("")

def add_arrays(names, files_with_name):
    result_data = np.zeros([7,5], dtype=int)
    for ii in names:
        array = files_with_name[ii]
        result_data = result_data + array
    return result_data

result_data = add_arrays(left, files_with_name)

result_df = pd.DataFrame(result_data, columns=columns_name)
print(result_df)
result_df.to_excel("/Users/liushiwen/Desktop/大四上/schedule.xlsx", index=False)
print(f"The total number of people: {len(files_with_name)}")

def check_people(col, row, arrays):
    name_list = []
    for name in arrays.keys():
        if arrays[name][row, col] == 1:
            # print(f"{name}, Row {row}, Column {col} contains 1")
            name_list.append(name)
    return name_list  
people_in = check_people(4, 0, files_with_name)
print(f"The Ok person in the phase: {len(people_in)}")
for name in people_in:
    print(name)
print("")
left = list(set(left) - set(people_in))
print(left)

result_data = add_arrays(left, files_with_name)
result_df = pd.DataFrame(result_data, columns=columns_name)
print(result_df)