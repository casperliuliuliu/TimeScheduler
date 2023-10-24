import os
import pandas as pd

# Define the folder path
folder_path = "/Users/liushiwen/Desktop/大四上/schedule"

# Initialize an empty list to store DataFrames
dataframes = []

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
            dataframes.append(df)
print(dataframes[0])
# You now have a list of DataFrames from the files in the folder
# You can access and manipulate them as needed.
