
# Online Eye-Tracking Experiment

This project is a web-based eye-tracking experiment built with **Flask**, **JavaScript**, **WebGazer.js**, **HTML**, and **Python**. It allows remote participants to complete a short calibration, view randomized images while listening to an audio prompt, and have their gaze data recorded in real-time.

All collected data (X and Y screen coordinates + timestamps) is automatically saved to an Excel file on the server after the experiment ends.

---

## 🔬 Features

- 🔴 Calibration using 9 clickable circles
- 🎥 Real-time gaze tracking using WebGazer.js
- 🎧 Audio playback synchronized with visual stimuli
- 🖼️ Randomized image placement and randomized trial types
- 📊 Reaction time detection (how quickly the participant finds the correct image)
- 📝 Demographics collection (ID, initials, age, gender, date)
- 📂 Automatic gaze data collection and Excel export per participant
- 📈 Automated local data analysis (reaction time bar chart and gaze scatter plot)
- 🕒 Supports 20 randomized trials (configurable)
- 🌐 Deployed using [Render](https://render.com)

---

## 🧠 Technologies Used

- Python 3.11
- Flask
- JavaScript + WebGazer.js
- HTML5/CSS3
- Pandas + OpenPyXL
- Matplotlib (for data visualization)
- Watchdog (for local auto-analysis)
- Render (for deployment)

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/LuisR-ecu/Onlline-Eyetracking.git
   cd Onlline-Eyetracking
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**
   ```bash
   python server.py
   ```

4. Open your browser and go to `http://localhost:5000`

---

## 🔍 Automating Local Data Analysis (Optional)

To automatically analyze and visualize data whenever a new Excel file is saved:

```bash
python watch_gaze_folder.py
```

This will automatically run `analyze_data.py` when new gaze data is saved.

---

## 📊 Manual Data Analysis

If you prefer to manually analyze data:

```bash
python analyze_data.py
```

This will:
- Automatically load the latest Excel file from `gaze_data/`
- Plot reaction time bar chart by trial
- Plot gaze scatter plot with time progression

---

## 📁 Project Structure

```
/static/         → Images and audio used in the experiment  
/templates/      → HTML frontend (index.html)  
server.py        → Flask backend server  
requirements.txt → Python dependencies  
gaze_data/       → Excel files with saved gaze tracking data  
analyze_data.py  → Creates reaction time and gaze plots  
watch_gaze_folder.py → Automatically runs analyze_data.py when new data is saved  
```

---

## 📂 Example Gaze Data

Each Excel file saved in the `gaze_data/` folder contains:
- `x` → X coordinate of gaze
- `y` → Y coordinate of gaze
- `time` → Timestamp (seconds)
- `normX` → Normalized X position
- `normY` → Normalized Y position
- `trial` → Trial number
- `audioType` → Silent / Fast audio / Slow audio
- `reactionTime` → Time until participant looked at the correct image
- `lookedAtTarget` → Boolean (True/False)

---

## 📦 Deployment

This project is deployed on [Render.com](https://render.com) and can be shared via a public link with participants.  
The experiment works in modern browsers with webcam access.

---

## 👤 Author

**Luis Ramirez**  
Undergraduate Research Assistant  
[B.A. in Computer Science - East Carolina University (2023–2026)](https://github.com/LuisR-ecu)  
📄 [Resume / Research Profile](https://www.linkedin.com/in/ramirez-luis-hernandez)

---

## 📌 Notes

- Ensure participants **allow webcam access** for WebGazer to function.
- Data is stored temporarily on Render. Download Excel files regularly or switch to cloud storage for persistence.
- Reaction time and gaze data can be plotted automatically or manually.
