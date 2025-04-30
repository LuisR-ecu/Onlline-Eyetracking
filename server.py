from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Ensure gaze_data folder exists
if not os.path.exists("gaze_data"):
    os.makedirs("gaze_data")

# Serve main experiment page
@app.route("/")
def index():
    return render_template("index.html")

# Handle incoming gaze data from the frontend
@app.route("/save_gaze", methods=["POST"])
def save_gaze():
    data = request.get_json()
    gaze = data.get("gaze", [])

    if not gaze:
        return jsonify({"status": "error", "message": "No gaze data received"}), 400

    # Convert to DataFrame
    df = pd.DataFrame(gaze)

    # Timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gaze_data/gaze_data_{timestamp}.xlsx"

    # Save to Excel
    df.to_excel(filename, index=False)

    print(f"✅ Received POST to /save_gaze")
    print(f"📦 Received {len(gaze)} gaze points")
    print(f"✅ Data written to: {filename}")

    return jsonify({"status": "success", "saved_to": filename}), 200

if __name__ == "__main__":
    app.run(debug=True)