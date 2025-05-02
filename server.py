from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Create a folder to save gaze data if it doesn't exist
if not os.path.exists('gaze_data'):
    os.makedirs('gaze_data')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_gaze', methods=['POST'])
def save_gaze():
    data = request.get_json()
    gaze = data['gaze']
    pid = data.get('participant_id', 'unknown')
    initials = data.get('initials', 'unknown')

    df = pd.DataFrame(gaze)

    # Save with timestamp, PID and initials
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gaze_data/gaze_data_{pid}_{initials}_{timestamp}.xlsx"
    df.to_excel(filename, index=False)

    print(f"✅ Data saved to {filename}")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)