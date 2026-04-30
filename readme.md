Drowsiness Detection System
A real-time Python application that monitors eye activity via a webcam. The system uses Haar Cascade Classifiers to detect whether eyes are open and triggers an audible alert if eyes are not detected for a specific duration.
🚀 Features
Real-time Detection: Uses OpenCV to process video frames instantly.
Visual Feedback: Draws bounding boxes around detected eyes and displays status text on the screen.
Audio Alert: Utilizes winsound to trigger a beep if no eyes are detected, acting as a safety warning for drowsiness.
🛠️ Prerequisites
Before running the script, ensure you have the following installed:
Python 3.x
OpenCV: pip install opencv-python
Windows OS: The current script uses winsound, which is a Windows-specific library.
📁 Project Structure
drowness_detection.py: The main script containing the detection logic and video capture loop.
haarcascade_eye.xml: Automatically loaded via OpenCV data path to identify eye patterns.
💻 How It Works
Grayscale Conversion: The video feed is converted to grayscale to simplify the data for the classifier.
Detection: The detectMultiScale function scans the frame for eye patterns.
Logic: * If no eyes are detected, the system pauses briefly and triggers a high-frequency beep (5000 Hz).
If eyes are detected, white rectangles are drawn around them, and the text "Eyes opened" is displayed.
Termination: Press the 'q' key to safely exit the application and release the camera.
