
# Online Eye-Tracking Experiment

This project is a web-based eye-tracking experiment using **Flask**, **JavaScript**, **WebGazer.js**, and **Python**. It lets participants complete calibration, view randomized trials with images and audio, and records their gaze data for reaction time and gaze pattern analysis.

All gaze data is saved automatically to Excel files for later analysis.

---

## 🔬 Features

- **Consent + Participant ID** collection before trials.
- **Calibration flow** with a dedicated instruction page, 9-point click targets, and optional on-screen accuracy check.
- **Real-time gaze tracking** via WebGazer.js.
- **Images + Audio stimuli** randomized across trials.
- **Flexible trial types**: silent, slow (casual audio), fast (rushed audio).
- **Pauses with instructions** between each trial.
- **Reaction time estimation** and gaze logging.
- **Automatic Excel export** of gaze data.
- **Graphing script** for reaction times & gaze scatter plots.
- **Participant metadata** saved with data files.

---

## 🧠 Technologies Used

- Python 3.11
- Flask
- JavaScript + WebGazer.js
- HTML5 / CSS3
- Pandas + OpenPyXL
- Matplotlib + Seaborn (for data analysis)
- Render (for online deployment)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/LuisR-ecu/Onlline-Eyetracking.git
cd Onlline-Eyetracking
pip install -r requirements.txt
python server.py
```

Then open your browser and visit:
```
http://localhost:5000
```

---

## 📁 Project Structure

```
/static/         → Images and audio files used in the experiment  
/templates/      → index.html (frontend interface)  
server.py        → Flask backend server  
analyze_data.py  → Script to analyze saved gaze data  
requirements.txt → Python dependencies  
gaze_data/       → Folder where Excel files are saved after each participant completes
```

---

## 🔍 Data Collected

Each gaze data Excel file contains:

- `x` → X coordinate (pixels)
- `y` → Y coordinate (pixels)
- `t` → Timestamp (milliseconds from trial start)
- `trial` → Trial number
- `type` → Trial type (silent, slow, fast)

---

## 📊 Data Analysis

After running an experiment, set the correct filename in `analyze_data.py` and run:

```bash
python analyze_data.py
```

You’ll get:

- **Reaction Time Plot** (first gaze timestamp per trial).
- **Gaze Scatter Plot** (XY positions colored by trial).

---

## 📝 Participant Journey

- **Landing & consent:** Participant enters ID, initials, age, and gender before continuing.
- **Calibration prep:** Dedicated instruction page explains webcam setup and how to complete the 9-point calibration.
- **Calibration & validation:** WebGazer.js guides participants through nine dots; researchers can enable an optional accuracy check by toggling `ENABLE_CALIBRATION_VALIDATION` in `templates/index.html`.
- **Guided practice:** Practice trials play COVID/colon sentences with matching images so participants learn the eye-only response pattern.
- **Experimental blocks:** Randomized trials with fixation crosses between each step.
- **Data save:** On completion, gaze traces and reaction metrics are written to Excel and background analysis is triggered.

### In-experiment Reminders

- **Silent** → Read each instruction and look at the matching image before continuing.
- **Slow/Fast** → Listen to the audio instruction and look at the matching image.

## ⚙️ Gaze Smoothing & Logging

To reduce webcam jitter while preserving reaction timing, the client averages the last few WebGazer predictions and throttles logging to once every `GAZE_LOG_INTERVAL_MS` (default 50 ms). Adjust these constants in `templates/index.html`:

- `GAZE_SMOOTHING_WINDOW`: number of recent samples (default 5) included in the moving average.
- `GAZE_LOG_INTERVAL_MS`: minimum milliseconds between saved gaze rows.

Set `ENABLE_CALIBRATION_VALIDATION = true` in the same file to show the post-calibration accuracy check overlay; leave it `false` for smoother testing sessions.

---

## 🌐 Deployment

This app is also configured for deployment on [Render.com](https://render.com)  
(Instructions and production configuration available on request).

---

## 👤 Author

**Luis Ramirez**  
Undergraduate Research Assistant  
[B.A. in Computer Science — East Carolina University (2023–2026)](https://github.com/LuisR-ecu)  
📄 [Resume / Research Profile](www.linkedin.com/in/ramirez-luis-hernandez)
