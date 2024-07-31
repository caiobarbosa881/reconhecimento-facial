import cv2 #opencv
import mediapipe as mp

# Inicializando o OpenCV e o MediaPipe
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Ler Info da Webcam
    verificador, frame = webcam.read()
    if not verificador:
        break
    # Reconhecer Rostos
    lista_rostos = reconhecedor_rostos.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(frame, rosto)
    cv2.imshow("Rostos na Webcam 1", frame)
    # ESC, para o Loop(ESC é a tecla número 27)
    if cv2.waitKey(5) == 27:
        break

webcam.release()
