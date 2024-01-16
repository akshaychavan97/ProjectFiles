import pandas as pd

# Input CSV file location
csv_file_location = input("Provide Input CSV File Location: ")

# Number of rows in each file
rows_per_file = int(input("Provide Number of Rows In Each File: "))

# Read the CSV file
df = pd.read_csv(csv_file_location)

# Split the DataFrame into chunks
chunks = [df[i:i + rows_per_file] for i in range(0, len(df), rows_per_file)]

# Save each chunk to a separate CSV file
for i, chunk in enumerate(chunks, start=1):
    output_file = f"output_file_{i}.csv"
    chunk.to_csv(output_file, index=False)
    print(f"File {output_file} created.")
