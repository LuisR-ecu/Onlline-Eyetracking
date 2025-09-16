from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime
import threading

# Import analyzer for auto-generation of plots/CSVs after save
import analyze_data

app = Flask(__name__)

if not os.path.exists('gaze_data'):
    os.makedirs('gaze_data')

@app.route('/')
def instructions():
    return render_template('instructions.html')


@app.route('/calibration')
def calibration():
    return render_template('index.html')

@app.route('/save_gaze', methods=['POST'])
def save_gaze():
    data = request.get_json()
    gaze = data.get('gaze', [])
    results = data.get('results', [])
    demographics = data.get('demographics', {})

    if not gaze and not results:
        print("⚠️ No data received — nothing saved.")
        return jsonify({'status': 'empty'}), 400

    gaze_df = pd.DataFrame(gaze) if gaze else pd.DataFrame()
    results_df = pd.DataFrame(results) if results else pd.DataFrame()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gaze_data/gaze_data_{demographics.get('pid', 'unknown')}_{demographics.get('initials', 'xx')}_{timestamp}.xlsx"

    with pd.ExcelWriter(filename) as writer:
        if not gaze_df.empty:
            gaze_df.to_excel(writer, index=False, sheet_name="Gaze Data")
        if not results_df.empty:
            results_df.to_excel(writer, index=False, sheet_name="Trial Results")
        pd.DataFrame([demographics]).to_excel(writer, index=False, sheet_name="Participant Info")

    print(f"✅ Data saved to {filename}")
    # Kick off analysis in the background for this file
    threading.Thread(target=analyze_data.process_file, args=(filename,), daemon=True).start()
    return jsonify({'status': 'success', 'file': filename})

if __name__ == '__main__':
    app.run(debug=True)
