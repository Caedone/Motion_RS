# Caedon Ewing
# Date: 6/25/2024
# This code aims to combine the Motion files by continuing the first file's Timestamp data  based on
# the numbers of rows in the other given files, incrementing by a number calculated by the difference between the
# last two rows of the first file


import pandas as pd

# Input the path to all files you want to combine:
csv_file_list = ["Testfile.csv","TestFile2.csv"]

# Input the path to where you want to store the result
output_file = r"Testresult.csv"

X = True  # Sets temp value to final_row value


# Function to read CSV file with the specified colum
def read_csv_file(file_path):
    return pd.read_csv(file_path, usecols=[2], header=None)


# Read each CSV file and store in globals
for i in range(len(csv_file_list)):
    globals()[f"df_{i}"] = read_csv_file(csv_file_list[i])

first_file = True  # Keeps track if the first file is being read in
for i in range(len(csv_file_list)):
    if first_file:
        df_name = globals()[f"df_{i}"]  # Retrieve the DataFrame object using globals()
        final_row = df_name.iloc[-1].astype(float).round(6)  # Stores the final row of the first file
        subtraction = final_row - df_name.iloc[-2].astype(float).round(6)# Subtracts the last two rows

        # Copies file to the output file
        df_name.to_csv(output_file, index=False, header=True)
        first_file = False


    else:
        df = globals()[f"df_{i}"]  # Retrieve the DataFrame object using globals()

        row_count = len(df)  # Gets the amount of rows in file
        if X:  # If initial iteration
            temp2 = final_row  # Copies the final row to temp variable

        # Initialize a list to accumulate row strings
        rows_to_write = []

        w = 0
        while w < row_count:
            sum_row = (temp2 + subtraction).astype(float).round(6)  # Add final row + the subtacted rows
            sum_row_str = sum_row.to_frame().T.to_csv(header=False, index=False).strip()  # Convert to CSV row string and strip newlines
            rows_to_write.append(sum_row_str)  # Add to list of rows to write
            temp2 = sum_row
            w += 1

        # Write all accumulated rows to the output file at once
        with open(output_file, 'a') as fd:
            fd.write("\n".join(rows_to_write) + "\n")  # Join rows with newline and write to file
        X = False



    # Read the final output to verify
print(pd.read_csv(output_file))