import cv2
import mediapipe as mp
import random
import math

# --- Initialization ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
frame_width = 1280
frame_height = 720
cap.set(3, frame_width)
cap.set(4, frame_height)

# --- Game Variables ---
fruits_and_bombs = [] # Renamed for clarity
spawn_counter = 0
score = 0

# --- Modified Fruit/Bomb Class ---
class GameObject: # Renamed class for clarity
    def __init__(self):
        self.x = random.randint(100, frame_width - 100)
        self.y = frame_height + 50
        self.vy = random.randint(-20, -10)
        self.radius = random.randint(30, 50)
        
        # --- NEW: Decide if it's a bomb (e.g., 20% chance) ---
        if random.random() < 0.2:
            self.is_bomb = True
            self.color = (0, 0, 0) # Bombs are black
        else:
            self.is_bomb = False
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Fruits are colorful
    
    def move(self):
        self.y += self.vy

    def draw(self, frame):
        cv2.circle(frame, (self.x, self.y), self.radius, self.color, -1)

# --- Main Game Loop ---
while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # --- Fruit/Bomb Spawning Logic ---
    spawn_counter += 1
    if spawn_counter >= 20:
        fruits_and_bombs.append(GameObject())
        spawn_counter = 0

    # --- Collision Detection Logic ---
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_fingertip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            tip_x = int(index_fingertip.x * frame_width)
            tip_y = int(index_fingertip.y * frame_height)
            cv2.circle(frame, (tip_x, tip_y), 15, (255, 255, 0), -1)

            # Check for collision with each object
            for obj in fruits_and_bombs[:]:
                distance = math.hypot(tip_x - obj.x, tip_y - obj.y)
                
                if distance < obj.radius:
                    # --- NEW: Check if the object is a bomb ---
                    if obj.is_bomb:
                        score = 0 # Reset score to zero
                        print("BOOM! 💥 Score reset.")
                    else:
                        score += 10 # Increase score for slicing a fruit
                    
                    fruits_and_bombs.remove(obj) # Remove the object regardless

    # --- Update and Draw Objects ---
    for obj in fruits_and_bombs:
        obj.move()
        obj.draw(frame)
    
    # Remove objects that go off-screen
    fruits_and_bombs = [obj for obj in fruits_and_bombs if obj.y > -obj.radius]

    # --- Display Score ---
    score_text = f"Score: {score}"
    cv2.putText(frame, score_text, (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4)

    cv2.imshow("Gesture Blade Game", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
cap.release()
cv2.destroyAllWindows()