import pandas as pd
import yaml

# Load the Excel file with multiple header rows and multiple indices
file_path = 'input.xlsx'
df = pd.read_excel(file_path, header=[0, 1], index_col=[0, 1])  # Adjust headers and index levels as needed


# Convert DataFrame to a nested dictionary structure
def df_to_nested_dict(df):
    nested_dict = {}
    for index, row in df.iterrows():
        d = nested_dict
        for level in index[:-1]:  # Handle multi-level index
            d = d.setdefault(level, {})
        d[index[-1]] = row.dropna().to_dict()  # Exclude NaN values
    return nested_dict


# Convert DataFrame to a dictionary
data_dict = df_to_nested_dict(df)

# Write the nested dictionary to a YAML file
output_yaml_file = 'output.yaml'
with open(output_yaml_file, 'w') as file:
    yaml.dump(data_dict, file, sort_keys=False, default_flow_style=False)

print(f"Data saved to {output_yaml_file}")
