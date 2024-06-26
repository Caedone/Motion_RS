# Caedon Ewing
# Date: 6/25/2024
# This code aims to combine the Motion files by continuing the first file's Timestamp data  based on
# the numbers of rows in the other given files, incrementing by a number calculated by the difference between the
# last two rows of the first file
# Requirements: Must have matlab engine api installed locally, use local interpreter


import matlab.engine
import pandas as pd
import numpy as np


X = True
# Starts the matlab engine
eng = matlab.engine.start_matlab()
First = ["Testfile3.csv"]
csv_file_list = ["Testfile3.csv", "Testfile.csv", "TestFile2.csv"]

# Handle for the first file
Mat_lab_handle = eng.triarea(First, nargout=0)

# Initialize a list to accumulate row strings
rows_to_write = []



df_first = pd.read_csv("combined_output.csv", usecols=[2], header=0)  # Tells to only read timestamp colum
final_row = df_first.iloc[-1].astype(float)  # Stores the final row of the first file
subtraction = final_row - df_first.iloc[-2].astype(float)  # Subtracts the last two rows
first_rows = len(df_first)  # Stores the length on first file timestamp colum
rows_to_write.extend(df_first.values.flatten().tolist())  # Append the entire first column to rows_to_write

at_lab_handle = eng.triarea(csv_file_list, nargout=0)
df = pd.read_csv("combined_output.csv")
third_column_name = df.columns[2]

row_count = len(df) - first_rows  # Gets the amount of rows in file
temp2 = final_row  # Copies the final row to temp variable

w = 0
while w < row_count:
    sum_row = (temp2 + subtraction).astype(float).round(6)  # Add final row + the subtracted rows
    rows_to_write.append(round(sum_row.item(), 6))  # Add to list of rows to write and round to 6 decimal places
    temp2 = sum_row
    w += 1


# Read the existing combined_output.csv file
combined_df = pd.read_csv("combined_output.csv")

# Replace the third column with the new data, formatted to display with 6 decimal places
combined_df.iloc[:, 2] = [f"{x:.6f}" for x in rows_to_write]

combined_df.replace(',,,,,,,,,', np.nan, regex=True, inplace=True)

# Write the updated DataFrame back to the CSV file
combined_df.to_csv("combined_output.csv", index=False)

#Close MATLAB engine
eng.quit()
