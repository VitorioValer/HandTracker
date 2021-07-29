import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

p_time = 0
c_time = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #  print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLns in results.multi_hand_landmarks:
            for i, lm in enumerate(handLns.landmark):
                #  print(i, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                print(i, cx, cy)

                # if id == 0:
                #     cv2.circle(img, )


            mpdraw.draw_landmarks(img, handLns, mphands.HAND_CONNECTIONS)

    c_time = time.time()
    fps = 1/(c_time - p_time)

    p_time = c_time

    cv2.putText(
        img, str(int(fps)),
        (10, 70), cv2.FONT_HERSHEY_PLAIN,
        3, (255, 0, 255),
        3
    )

    cv2.imshow('image', img)
    cv2.waitKey(1)
