:: -------------------------------------------- ::
::      README - DROWSINESS DETECTION SYSTEM    ::
:: -------------------------------------------- ::

:: STEP 1: Go to your project directory
cd path/to/Drowsiness_Detection_Project

:: STEP 2: Install required dependencies (skip if already installed)
pip install opencv-python imutils pygame scipy numpy

:: STEP 3: (If NOT installed) Install CMake
:: - Download from: https://cmake.org/download/
:: - During installation, make sure to CHECK:
::   "Add CMake to system PATH for all users"

:: STEP 4: Install dlib (after CMake and Build Tools are ready)
pip install dlib

:: STEP 5: Ensure the following files are in the same folder:
   - drowsiness_detection.py
   - shape_predictor_68_face_landmarks.dat
   - alert.mp3
   - absence.wav

:: Download resources:
   - Shape predictor model:
     http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
   - Audio files (alert & absence):
     https://www.transfernow.net/dl/20250609ugHMMvjv
:: Extract and place them in the project folder.

:: STEP 6: Run the Python script
python drowsiness_detection.py

:: -------------------------------------------- ::
::                  CONTROLS                   ::
:: -------------------------------------------- ::
:: - The webcam will start automatically
:: - Press 'q' to quit the application

:: -------------------------------------------- ::
::             ABOUT THE PROJECT               ::
:: -------------------------------------------- ::
:: This system detects drowsiness in real-time using webcam.
:: It tracks facial landmarks to monitor:
::   👁️  Eye Aspect Ratio (EAR)
::   👄  Mouth Aspect Ratio (MAR)

:: ⚙️  Features:
   - 🔔 Alerts when eyes remain closed too long (drowsiness)
   - 🥱 Alerts when yawning is detected
   - 🚫 Alerts when no face is detected for a certain time

:: 🛠️  Technologies Used:
   - Python
   - OpenCV
   - dlib
   - pygame
   - imutils
   - scipy
   - numpy

:: 👨‍💻 Author: Mukul Mehra
:: 🔗 GitHub: https://github.com/muks79
:: 📧 Email : mukulmehra681@gmail.com

:: -------------------------------------------- ::
::                Happy Coding!                ::
:: -------------------------------------------- ::
