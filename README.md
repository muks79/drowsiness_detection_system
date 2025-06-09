:: --------------------------------------------
:: README - DROWSINESS DETECTION SYSTEM SETUP
:: --------------------------------------------

:: 1. Go to your project directory

:: 2. Install dependencies (skip ones you already have)
pip install opencv-python imutils pygame scipy numpy

:: 3. (IF NOT INSTALLED) Install CMake to help with dlib build
:: Download and install manually from: https://cmake.org/download/
:: During installation, CHECK “Add CMake to system PATH for all users”

:: 4. Install dlib after CMake and Build Tools are installed
pip install dlib

:: 5. Make sure these files are in the same folder:
:: - drowsiness_detection.py
:: - shape_predictor_68_face_landmarks.dat
:: - alert.mp3
:: - absence.wav

:: Download .dat file from: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
:: Extract it and place the .dat file here.

:: 7. Run the Python script
python drowsiness_detection.py

:: --------------------------------------------
:: Controls:
:: - Webcam will start
:: - Press 'q' to quit
:: --------------------------------------------

:: ABOUT THE PROJECT
:: -----------------
:: This project detects user drowsiness using webcam by monitoring:
:: 👁️ Eye Aspect Ratio (EAR)
:: 👄 Mouth Aspect Ratio (MAR)
:: If eyes stay closed or yawning is detected, an alert plays.
:: If no face is detected for a while, another sound is played.

:: Built using: Python, OpenCV, dlib, pygame, Tkinter (for GUI, optional)
:: Author: Mukul Mehra
:: GitHub: https://github.com/muks79
:: Email: mukulmehra681@gmail.com

:: --------------------------------------------
:: Happy Coding!
:: --------------------------------------------
