import pandas as pd

# Load the dataset
df = pd.read_csv("../admin.csv")

# Filter rows for Gen Z
gen_z_df = df[df['label'] == 'Gen Z']

# Filter rows for Non-Gen Z
non_gen_z_df = df[df['label'] == 'Non-Gen Z']

# Save the filtered data into separate CSV files
gen_z_df.to_csv('gen_z.csv', index=False)
non_gen_z_df.to_csv('non_gen_z.csv', index=False)

print("Data has been separated and saved into 'gen_z.csv' and 'non_gen_z.csv'")
