import os
import pandas as pd

data = {
    "A": [1, 2, 3, 4, 5],
    "B": [5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)

# target folder path
folder_path = r"C:\Users\Z.S computers\Desktop\pc\project\db"

# create folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# full file path
file_path = os.path.join(folder_path, "data.csv")

# save csv
df.to_csv(file_path, index=False)

print("Saved at:", file_path)
