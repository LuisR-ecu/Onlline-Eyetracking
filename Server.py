from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = "gaze_data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save_gaze", methods=["POST"])
def save_gaze():
    data = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(DATA_DIR, f"gaze_data_{timestamp}.xlsx")

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

    return jsonify({"message": "Data saved successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)