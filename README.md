Hand Tracker using OpenCV and MediaPipe

This Python script uses OpenCV and MediaPipe to detect and track hands in real-time through your webcam. It also counts the number of fingers that are extended and displays the count on the video feed.

Features

Real-time hand detection.

Tracks landmarks of each hand.

Counts the number of fingers that are raised.

Visualizes hand landmarks and connections on the video feed.

Requirements

Python 3.7+

OpenCV (opencv-python)

MediaPipe (mediapipe)

You can install the dependencies using pip:

pip install opencv-python mediapipe

How to Run

Connect a webcam to your computer.

Save the script as hand_tracker.py.

Run the script:

python hand_tracker.py


A window named "Hand Tracker" will appear showing your hand with landmarks drawn and the number of extended fingers displayed.

Press ESC to exit the program.

How It Works

Captures video from the webcam using OpenCV.

Converts each frame to RGB and processes it with MediaPipe Hands.

Detects landmarks for each hand.

Uses the landmarks to determine which fingers are up:

Thumb: checks horizontal position.

Other fingers: checks vertical position.

Displays the count of raised fingers on the video feed.

Draws hand landmarks and connections for better visualization.

Notes

Make sure you have proper lighting for better hand detection.

The script flips the camera feed horizontally to make it mirror-like.

Currently counts a maximum of 5 fingers per hand.
