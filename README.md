# Online Eye-Tracking Experiment

This project is a web-based eye-tracking experiment built with **Flask**, **JavaScript**, **WebGazer.js**, **HTML**, and **Python**. It allows remote participants to complete a short calibration, view randomized images while listening to an audio prompt, and have their gaze data recorded in real-time.

All collected data (X and Y screen coordinates + timestamps) is automatically saved to an Excel file on the server after the experiment ends.

---

## 🔬 Features

- 🔴 Calibration using 9 clickable circles
- 🎥 Real-time gaze tracking using WebGazer.js
- 🎧 Audio playback synchronized with visual stimuli
- 🖼️ Randomized image placement in the 4 corners of the screen
- 📊 Automatic gaze data collection and Excel export
- 🌐 Deployed using [Render](https://render.com)

---

## 🧠 Technologies Used

- Python 3.11
- Flask
- JavaScript + WebGazer.js
- HTML5/CSS3
- Pandas + OpenPyXL
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

## 📁 Project Structure

```
/static/         → Images and audio used in the experiment  
/templates/      → HTML frontend (index.html)  
server.py        → Flask backend server  
requirements.txt → Python dependencies  
gaze_data/       → Excel files with saved gaze tracking data  
```

---

## 📂 Example Gaze Data

Each Excel file saved in the `gaze_data/` folder contains:
- `x` → X coordinate of gaze on screen
- `y` → Y coordinate of gaze
- `time` → Timestamp in milliseconds

---

## 📦 Deployment

This project is deployed on [Render.com](https://render.com) and can be shared via a public link with participants. The experiment works in modern browsers with webcam access.

---

## 👤 Author

**Luis Ramirez**  
Undergraduate Research Assistant  
[B.A. in Computer Science - East Carolina University (2023–2026)](https://github.com/LuisR-ecu)  
📄 [Resume / Research Profile](https://example.com/luis-resume-or-profile)

---

## 📌 Notes

- Ensure participants **allow webcam access** for WebGazer to work.
- Data is only stored temporarily on Render. To persist it, download the Excel file immediately or integrate with cloud storage.
