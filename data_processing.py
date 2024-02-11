import pandas as pd

# Path to the downloaded CSV file
csv_file_path = r"C:\Users\Admin\Desktop\InternCareer\WHO_Global_TB_data.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Display the original DataFrame
print("Original DataFrame:")
print(df.head())

# Data Processing Techniques
# 1. Handling Missing Values
# Drop rows with any missing values
processed_df = df.dropna()

# 2. Data Transformation
# Convert string columns to lowercase
string_columns = df.select_dtypes(include=['object']).columns
df[string_columns] = df[string_columns].apply(lambda x: x.str.lower())

# 3. Data Aggregation
# Group by 'country' and calculate the mean of 'new_sp_cases'
aggregated_df = df.groupby('country')['new_sp_cases'].mean().reset_index()

# 4. Data Filtering
# Filter rows based on a condition
filtered_df = df[df['new_sp_cases'] > 100]

# Display the processed DataFrames
print("\nProcessed DataFrames:")
print("Processed DataFrame with missing values removed:")
print(processed_df.head())

print("\nProcessed DataFrame with string columns converted to lowercase:")
print(df.head())

print("\nAggregated DataFrame with mean 'new_sp_cases' per country:")
print(aggregated_df.head())

print("\nFiltered DataFrame with 'new_sp_cases' greater than 100:")
print(filtered_df.head())

# Save the processed DataFrames to CSV files
processed_df.to_csv(r"C:\Users\Admin\Desktop\InternCareer\processed_data.csv", index=False)
aggregated_df.to_csv(r"C:\Users\Admin\Desktop\InternCareer\aggregated_data.csv", index=False)
filtered_df.to_csv(r"C:\Users\Admin\Desktop\InternCareer\filtered_data.csv", index=False)
