import pandas as pd

# Load collected data
df = pd.read_csv("process_dataset.csv")

# Drop process names (not needed for ML)
df = df.drop(columns=['Process_Name'])

# Save preprocessed data
df.to_csv("cleaned_data.csv", index=False)
print("[INFO] Data preprocessed and saved to cleaned_data.csv")
