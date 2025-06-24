import cv2 as cv
import mediapipe as mp

mpFace = mp.solutions.face_detection
face = mpFace.FaceDetection(0.70)

cap = cv.VideoCapture(0)

while True:
    succes, frame = cap.read()
    
    if not succes:
        break

    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = face.process(frameRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            print(bboxC)
            
            fh, fw, _ = frame.shape

            rw1 = int(bboxC.xmin * fw)
            rh1 = int(bboxC.ymin * fh)
            w = int(bboxC.width * fw)
            h = int(bboxC.height * fh)
            rw2 = rw1 + w
            rh2 = rh1 + h

            cv.rectangle(frame, (rw1, rh1), (rw2, rh2), (0, 255, 0), 2)


    cv.imshow("face-detection", frame)

    quit = cv.waitKey(1)
    if quit != -1:
        break