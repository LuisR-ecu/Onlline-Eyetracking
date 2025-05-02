from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
import random
from datetime import datetime

app = Flask(__name__)

# Number of trials can easily be changed here
NUM_TRIALS = 20

# Define trial pool (silent, slow, fast with corresponding images/audio)
TRIAL_POOL = [
    {"type": "silent", "audio": None, "images": ["dropper.png", "swab.png", "test_tube.png", "test_cassette.png"], "text": "Read: Find the test tube"},
    {"type": "slow", "audio": "all_casual.wav", "images": ["swab.png", "test_cassette.png", "dropper.png", "test_tube.png"], "text": "Find the swab"},
    {"type": "fast", "audio": "all_fast.wav", "images": ["test_cassette.png", "dropper.png", "swab.png", "test_tube.png"], "text": "Find the cassette"},
    # You can add more variations here
]

# Randomize trials from the pool
def generate_trials():
    return [random.choice(TRIAL_POOL) for _ in range(NUM_TRIALS)]

@app.route('/')
def index():
    trials = generate_trials()
    return render_template('index.html', trials=trials)

@app.route('/save_gaze', methods=['POST'])
def save_gaze():
    data = request.get_json()
    gaze = data['gaze']
    participant_id = data.get('participant_id', 'unknown')
    initials = data.get('initials', '')

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gaze_data/gaze_{participant_id}_{initials}_{timestamp}.xlsx"

    df = pd.DataFrame(gaze)
    if not os.path.exists('gaze_data'):
        os.makedirs('gaze_data')
    df.to_excel(filename, index=False)

    print(f"✅ Data saved to {filename}")
    return jsonify({"status": "success", "file": filename})

if __name__ == '__main__':
    app.run(debug=True)