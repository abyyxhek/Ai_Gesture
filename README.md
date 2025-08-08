

Gesture Blade Game ⚔️
This is a fun, interactive game where you use your hand as a virtual blade to slice fruits and avoid bombs. The entire game is controlled by your hand's movement, tracked in real-time through your webcam.

📝 Description
Gesture Blade uses the power of computer vision to create an immersive gaming experience without the need for a keyboard, mouse, or controller. The application detects your hand and allows you to interact with game objects flying across the screen. Slice colorful fruits to increase your score, but be careful not to hit the bombs, or your score will reset!

✨ Features
Real-Time Hand Tracking: Utilizes Google's MediaPipe library to accurately detect and track your hand's position and landmarks.

Gesture-Based Control: Your index finger acts as the virtual "blade."

Dynamic Objects: The game randomly spawns colorful fruits and black bombs that fly up the screen.

Collision Detection: Instantly detects when your hand "slices" through an object.

Scoring System: Gain 10 points for every fruit sliced. Hit a bomb, and your score resets to zero!

🛠️ How It Works
The project is built entirely in Python and relies on two main libraries:

OpenCV: This library is used to capture the live video feed from your webcam and to draw all the game elements (fruits, bombs, score, and the indicator on your fingertip).

MediaPipe: This is the core AI engine. It processes each frame of the video to find the precise location of your hand's key points (landmarks). We use the coordinate of the index fingertip to determine the position of the "blade."

🚀 Getting Started
Follow these instructions to get the game running on your local machine.

Prerequisites
You need to have Python installed on your system. Then, install the required libraries by running the following command in your terminal:

pip install opencv-python mediapipe
Running the Game
Save the game code as a Python file (e.g., gesture_blade.py).

Open a terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script with the following command:

 
python gesture_blade.py


🎮 How to Play
When the game window opens, position yourself so your hand is clearly visible to the webcam.

Move your hand to "slice" the colorful circles (fruits) as they fly up the screen.

Avoid touching the black circles (bombs).

Your score is displayed in the top-left corner.

To quit the game, make sure the game window is active and press the 'q' key on your keyboard.
