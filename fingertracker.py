import cv2
import mediapipe as mp  
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils 

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB) 
    lmList = []
    counter = 0
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  
                if len(lmList) == 21:
                    for i in (4,8,12,16,20):
                        if i == 4:
                            if lmList[i][1] < lmList[i - 2][1]:
                                counter += 1
                        else:
                            if lmList[i][2] < lmList[i - 2][2]:
                                counter += 1
                    cv2.putText(img, str(counter), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Hand Tracker", img)
    if cv2.waitKey(5) & 0xFF == 27:
        break