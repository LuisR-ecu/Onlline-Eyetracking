import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.switch_backend('Agg')  # Use headless backend for server environments

gaze_data_dir = 'gaze_data'

def assign_quadrant(x, y, screen_width, screen_height):
    if x < screen_width / 2 and y < screen_height / 2:
        return 'Top-Left'
    elif x >= screen_width / 2 and y < screen_height / 2:
        return 'Top-Right'
    elif x < screen_width / 2 and y >= screen_height / 2:
        return 'Bottom-Left'
    else:
        return 'Bottom-Right'

for file in os.listdir(gaze_data_dir):
    if file.endswith('.xlsx'):
        filepath = os.path.join(gaze_data_dir, file)
        print(f"📄 Processing: {file}")
        df = pd.read_excel(filepath, sheet_name='Gaze Data')

        df['time'] = pd.to_numeric(df['time'], errors='coerce')
        df = df.dropna(subset=['time', 'x', 'y'])

        df['bin'] = (df['time'] // 5).astype(int)
        binned = df.groupby(['trial', 'bin']).agg({
            'x': 'mean',
            'y': 'mean',
            'reactionTime': 'first',
            'lookedAtTarget': 'max'
        }).reset_index()

        screen_width = 1280
        screen_height = 720
        binned['quadrant'] = binned.apply(lambda row: assign_quadrant(row['x'], row['y'], screen_width, screen_height), axis=1)

        # Reaction Time Plot
        rt_plot = binned[binned['lookedAtTarget'] == True].groupby('trial')['reactionTime'].first()
        plt.figure(figsize=(10, 5))
        rt_plot.plot(kind='bar')
        plt.title('Reaction Time by Trial')
        plt.ylabel('Seconds')
        plt.xlabel('Trial')
        plt.tight_layout()
        plt.savefig(filepath.replace('.xlsx', '_reaction_time.png'))
        plt.close()

        # Quadrant Scatter Plot
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=binned, x='x', y='y', hue='quadrant', palette='tab10')
        plt.gca().invert_yaxis()
        plt.title('Binned Gaze Points by Quadrant')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.tight_layout()
        plt.savefig(filepath.replace('.xlsx', '_quadrants.png'))
        plt.close()

        print("✅ Saved plots for", file)