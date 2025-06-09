import tkinter as tk
from tkinter import messagebox, ttk
import threading
import cv2
import dlib
import imutils
from scipy.spatial import distance
from imutils import face_utils
from pygame import mixer
import os

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def mouth_aspect_ratio(mouth):
    A = distance.euclidean(mouth[2], mouth[10])
    B = distance.euclidean(mouth[4], mouth[8])
    C = distance.euclidean(mouth[0], mouth[6])
    return (A + B) / (2.0 * C)

class DrowsinessDetection:
    def __init__(self, shape_predictor, alert_sound, absence_sound):
        self.running = False
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(shape_predictor)
        mixer.init()
        mixer.music.load(alert_sound)
        self.absence_alert = mixer.Sound(absence_sound)
        self.alert_playing = False

    def start_detection(self, config):
        self.running = True
        cap = cv2.VideoCapture(0)
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
        (mStart, mEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["mouth"]
        absence_flag, drowsy_flag = 0, 0
        user_name = "Mukul"

        while self.running:
            ret, frame = cap.read()
            if not ret:
                print("Webcam not accessible.")
                break

            frame = imutils.resize(frame, width=900)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            subjects = self.detector(gray, 0)

            if len(subjects) == 0:
                absence_flag += 1
                if absence_flag > config["absence_threshold"]:
                    cv2.putText(frame, "NO USER DETECTED!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    if not self.alert_playing:
                        self.absence_alert.play()
                        self.alert_playing = True
                else:
                    absence_flag = 0
                    self.alert_playing = False

            for subject in subjects:
                shape = self.predictor(gray, subject)
                shape = face_utils.shape_to_np(shape)
                left_eye = shape[lStart:lEnd]
                right_eye = shape[rStart:rEnd]
                ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0
                mouth = shape[mStart:mEnd]
                mar = mouth_aspect_ratio(mouth)

                cv2.drawContours(frame, [cv2.convexHull(left_eye)], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [cv2.convexHull(right_eye)], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [cv2.convexHull(mouth)], -1, (255, 0, 0), 1)

                x, y = subject.left(), subject.top()
                cv2.putText(frame, user_name, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

                if ear < config["ear_threshold"]:
                    drowsy_flag += 1
                    if drowsy_flag >= config["frame_check"]:
                        cv2.putText(frame, "ALERT! DROWSINESS DETECTED!", (10, 60),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        if not mixer.music.get_busy():
                            mixer.music.play()
                else:
                    drowsy_flag = 0

                if mar > config["yawn_threshold"]:
                    cv2.putText(frame, "ALERT! YAWNING DETECTED!", (10, 90),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            cv2.imshow("Drowsiness Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = DrowsinessDetection("shape_predictor_68_face_landmarks.dat", "alert.mp3", "absence.wav")
    config = {
        "ear_threshold": 0.25,
        "yawn_threshold": 0.75,
        "frame_check": 20,
        "absence_threshold": 30
    }
    detector.start_detection(config)
