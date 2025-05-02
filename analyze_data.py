import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

# -------- CONFIG --------
DATA_FOLDER = "gaze_data"
# Replace this with the filename of the session you want to analyze:
FILENAME = "your_file_here.xlsx"
# ------------------------

# Load the data
filepath = os.path.join(DATA_FOLDER, FILENAME)
df = pd.read_excel(filepath)

print("Data loaded:")
print(df.head())

# -------- Reaction Time Plot --------
plt.figure(figsize=(10, 5))
reaction_times = df.groupby("trial")["t"].min() / 1000  # Convert ms to seconds
reaction_times.plot(kind='bar')
plt.xlabel("Trial")
plt.ylabel("First gaze timestamp (s)")
plt.title("Reaction Time per Trial")
plt.tight_layout()
plt.show()

# -------- Gaze Scatter Plot --------
plt.figure(figsize=(8, 6))
sns.scatterplot(x="x", y="y", hue="trial", data=df, palette="tab10")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Gaze Scatter Plot by Trial")
plt.gca().invert_yaxis()  # Flip Y axis to match screen coordinates
plt.legend(title="Trial")
plt.tight_layout()
plt.show()