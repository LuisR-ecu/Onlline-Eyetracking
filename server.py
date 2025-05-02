from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

if not os.path.exists('gaze_data'):
    os.makedirs('gaze_data')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_gaze', methods=['POST'])
def save_gaze():
    data = request.get_json()
    gaze = data['gaze']
    demographics = data['demographics']

    df = pd.DataFrame(gaze)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gaze_data/gaze_data_{demographics['pid']}_{demographics['initials']}_{timestamp}.xlsx"

    with pd.ExcelWriter(filename) as writer:
        df.to_excel(writer, index=False, sheet_name="Gaze Data")
        pd.DataFrame([demographics]).to_excel(writer, index=False, sheet_name="Participant Info")

    print(f"✅ Data saved to {filename}")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)