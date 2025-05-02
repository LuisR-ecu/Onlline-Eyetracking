
# Online Eye-Tracking Experiment

This project is a web-based eye-tracking experiment using **Flask**, **JavaScript**, **WebGazer.js**, and **Python**. It lets participants complete calibration, view randomized trials with images and audio, and records their gaze data for reaction time and gaze pattern analysis.

All gaze data is saved automatically to Excel files for later analysis.

---

## 🔬 Features

- **Consent + Participant ID** collection before trials.
- **Calibration** using 9 evenly spaced clickable points.
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

## 📝 Participant Instructions (for pauses between trials)

- **Silent** → Read each instruction and look at the matching image before continuing.
- **Slow/Fast** → Listen to the audio instruction and look at the matching image.

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
