:: -------------------------------------------- ::
::      README - DROWSINESS DETECTION SYSTEM    ::
:: -------------------------------------------- ::

:: 1. Go to your project directory
cd path/to/Drowsiness_Detection_Project

:: 2. Install required dependencies (skip if already installed)
pip install opencv-python imutils pygame scipy numpy

:: 3. (If NOT already installed) Install CMake
:: Download from: https://cmake.org/download/
:: IMPORTANT: During installation, CHECK the box
:: “Add CMake to system PATH for all users”

:: 4. Install dlib (after CMake and Build Tools are installed)
pip install dlib

:: 5. Make sure the following files are in the same folder:
   - drowsiness_detection.py
   - shape_predictor_68_face_landmarks.dat
   - alert.mp3
   - absence.wav

:: Download the .dat model from:
   http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
:: Extract the file and place it in the project folder.

:: 6. Run the Python script
python drowsiness_detection.py

:: -------------------------------------------- ::
::                 CONTROLS                    ::
:: -------------------------------------------- ::
:: - The webcam will start automatically
:: - Press 'q' to quit the application

:: -------------------------------------------- ::
::             ABOUT THE PROJECT               ::
:: -------------------------------------------- ::
:: This system detects user drowsiness in real-time via webcam
:: by analyzing:
::   👁️  Eye Aspect Ratio (EAR)
::   👄  Mouth Aspect Ratio (MAR)
::
:: Features:
:: - Alerts when eyes are closed too long (drowsiness)
:: - Alerts when yawning is detected
:: - Alerts when user is absent from camera view
::
:: Technologies Used:
:: Python, OpenCV, dlib, pygame, imutils, scipy, numpy

:: Author: Mukul Mehra
:: GitHub: https://github.com/muks79
:: Email : mukulmehra681@gmail.com

:: -------------------------------------------- ::
::                Happy Coding!                ::
:: -------------------------------------------- ::
