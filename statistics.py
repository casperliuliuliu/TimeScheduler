import os
import pandas as pd


# Define a function to validate each value
def validate_value(value):
    if value in [0, 1] and isinstance(value, int):
        return True
    return False

# Define the folder path
folder_path = "/Users/liushiwen/Desktop/大四上/schedule"

data = {
    'mon': [0, 0, 0, 0, 0, 0, 0],
    'tue': [0, 0, 0, 0, 0, 0, 0],
    'wed': [0, 0, 0, 0, 0, 0, 0],
    'thu': [0, 0, 0, 0, 0, 0, 0],
    'fri': [0, 0, 0, 0, 0, 0, 0]
}
temp_df = pd.DataFrame(data)
result_data = temp_df.to_numpy()

# # Initialize an empty list to store DataFrames
# dataframes = []
# filenames = []
# List all files in the folder
print(os.listdir(folder_path))
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
                print("All values in the DataFrames are valid (belong to {0, 1} and are integers).")
            else:
                print(f"There are invalid values in the DataFrames of [{filename}]")
            array = df.to_numpy()
            result_data = result_data + array
            # filenames.append(filename)
            # dataframes.append(df)
result_df = pd.DataFrame(result_data, columns=temp_df.columns)
result_df.to_excel("/Users/liushiwen/Desktop/大四上/schedule.xlsx", index=False)
print(result_df)
