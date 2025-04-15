from flask import Flask, render_template, request, jsonify, send_from_directory
from datetime import datetime
import os
import pandas as pd

app = Flask(__name__)
os.makedirs("gaze_data", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save_gaze", methods=["POST"])
def save_gaze():
    data = request.json
    print("✅ Received POST to /save_gaze")

    if not data:
        print("⚠️ No gaze data received!")
        return jsonify({"message": "No data received"}), 400

    print(f"📦 Received {len(data)} gaze points")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"gaze_data_{timestamp}.xlsx"
    filepath = os.path.join("gaze_data", filename)

    try:
        df = pd.DataFrame(data)
        df.to_excel(filepath, index=False)
        print(f"✅ Data written to: {filepath}")
        return jsonify({
            "message": "Data saved",
            "download_url": f"/download/{filename}"
        }), 200
    except Exception as e:
        print("❌ Error saving data:", e)
        return jsonify({"message": "Failed to save data"}), 500

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory("gaze_data", filename, as_attachment=True)