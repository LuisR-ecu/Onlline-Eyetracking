from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Ensure directory exists
if not os.path.exists("gaze_data"):
    os.makedirs("gaze_data")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save_gaze", methods=["POST"])
def save_gaze():
    data = request.get_json()
    gaze = data.get("gaze", [])
    participant_id = data.get("participant_id", "unknown")
    initials = data.get("initials", "")

    if not gaze:
        return jsonify({"status": "error", "message": "No gaze data received"}), 400

    # Save to Excel
    df = pd.DataFrame(gaze)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Safe file naming
    safe_id = str(participant_id).replace(" ", "_")
    safe_initials = str(initials).replace(" ", "_")

    filename = f"gaze_data/{safe_id}_{safe_initials}_{timestamp}.xlsx"
    df.to_excel(filename, index=False)

    print(f"✅ Received POST to /save_gaze")
    print(f"🧑‍💻 Participant: {participant_id} ({initials})")
    print(f"📦 Received {len(gaze)} gaze points")
    print(f"✅ Data written to: {filename}")

    return jsonify({"status": "success", "saved_to": filename}), 200

if __name__ == "__main__":
    app.run(debug=True)