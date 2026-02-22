<h1 align="center">
Virtual Cube Writer
</h1>

<h3 align="center">
A Real-Time Computer Vision Entertainment System
</h3>

---

## <span style="color:#4EA1FF">PROJECT OVERVIEW</span>

Virtual Cube Writer is a real-time computer vision entertainment application that enables users to build digital structures using only hand gestures captured via webcam.

The system integrates hand tracking, gesture recognition, spatial grid logic, and real-time analytics to create a fully touchless and immersive interactive experience.

This project demonstrates applied AI in an interactive and visually engaging environment.

---

## <span style="color:#4EA1FF">CORE FEATURES</span>

### <span style="color:#00C896">Real-Time Hand Tracking</span>

- Detection and separation of left and right hands
- Precise landmark extraction
- Smooth gesture recognition pipeline
- Optimized for real-time performance

---

### <span style="color:#00C896">Gesture-Based Interaction</span>

✋✋ Open hands → Open main menu

(left hand) ✋ + (right hand) 🤏 Pinch → Place structure

(left hand) ✊ + (right hand) 🤏 Fist + pinch → Delete structure

All interactions are processed live with minimal latency.

---

### <span style="color:#00C896">Construction Engine</span>

Users can dynamically create:

- Single cubes
- Walls
- Towers
- Stairs

Each structure automatically snaps to a dynamic spatial grid for precise alignment and consistency.

---

### <span style="color:#00C896">Real-Time Analytics System</span>

- FPS monitoring
- Cube counter
- Session duration tracking
- Performance feedback

---

## <span style="color:#4EA1FF">TECHNICAL ARCHITECTURE</span>

### Backend

- Python
- OpenCV
- MediaPipe

### System Design

- Modular architecture
- Real-time rendering engine
- Gesture processing pipeline
- Performance monitoring module

The project follows clean separation of concerns across:

- camera
- hands
- gestures
- construction
- rendering
- analytics
- utils

---

## <span style="color:#4EA1FF">INSTALLATION GUIDE</span>

### 1. Clone the repository

```bash
git clone https://github.com/abdennour-tr/Virtual-Cube-Engine.git
cd Virtual-Cube-Engine
```
### 2. Create a virtual environment
```bash
python -m venv venv
```

### Activate it:
#### Windows
```bash
venv\Scripts\activate
```

#### Linux
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python main.py
```





