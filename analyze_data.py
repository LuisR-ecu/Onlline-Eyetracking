import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# --- Automatically find the latest Excel file ---
list_of_files = glob.glob('gaze_data/*.xlsx')
if not list_of_files:
    raise FileNotFoundError("No Excel files found in gaze_data folder.")
filename = max(list_of_files, key=os.path.getctime)

print(f"📊 Loading latest data file: {filename}")

# --- Read gaze data ---
df = pd.read_excel(filename, sheet_name="Gaze Data")

# --- Reaction Time Plot ---
reaction_times = df[df['lookedAtTarget'] == True].groupby('trial')['reactionTime'].first()

plt.figure(figsize=(10, 6))
reaction_times.plot(kind='bar', color='skyblue')
plt.title('Reaction Time by Trial')
plt.ylabel('Seconds')
plt.xlabel('Trial')
plt.tight_layout()
plt.show()

# --- Gaze Scatter ---
plt.figure(figsize=(8, 6))
scatter = plt.scatter(df['x'], df['y'], c=df['time'], cmap='viridis', s=20)
plt.title('Gaze Points Over Time')
plt.xlabel('X position (pixels)')
plt.ylabel('Y position (pixels)')
plt.gca().invert_yaxis()
plt.colorbar(scatter, label='Time (s)')
plt.tight_layout()
plt.show()