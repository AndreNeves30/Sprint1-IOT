import cv2
import mediapipe as mp
import serial
import time

#arduino = serial.Serial('COM5', 9600, timeout=1)
#time.sleep(2)

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(max_num_faces=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Controle olhos
piscadas = 0
frames_fechado = 0
LIMIAR_FECHAR = 0.38
LIMIAR_ABRIR = 0.42

# Controle boca
boca_aberta = False
aberturas_boca = 0
LIMIAR_MAR_ABRIR = 0.60    
LIMIAR_MAR_FECHAR = 0.50

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = face_mesh.process(rgb)

    if resultados.multi_face_landmarks:
        pts = resultados.multi_face_landmarks[0].landmark

        mp_draw.draw_landmarks(
            frame,
            resultados.multi_face_landmarks[0],
            mp_face.FACEMESH_TESSELATION,
            landmark_drawing_spec=mp_draw.DrawingSpec(color=(255, 255, 0), thickness=1, circle_radius=1),
            connection_drawing_spec=mp_draw.DrawingSpec(color=(255, 255, 0), thickness=1)
        )

        # ----------------- EAR (Piscar) -----------------
        h = abs(pts[33].x - pts[133].x)
        v1 = abs(pts[159].y - pts[145].y)
        v2 = abs(pts[158].y - pts[153].y)
        ear = (v1 + v2) / (2.0 * h)

        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if ear <= LIMIAR_FECHAR:
            frames_fechado += 1
            if frames_fechado == 3:
                piscadas += 1
                #arduino.write(b'G')
        elif ear > LIMIAR_ABRIR:
            frames_fechado = 0

        cv2.putText(frame, f"PISCADAS: {piscadas}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # ----------------- MAR (Abertura da boca) -----------------
        # Pontos principais da boca no FaceMesh:
        # 13 = lábio superior
        # 14 = lábio inferior
        # 78 e 308 = cantos da boca

        boca_v = abs(pts[13].y - pts[14].y)       # Distância vertical
        boca_h = abs(pts[78].x - pts[308].x)      # Distância horizontal
        mar = boca_v / boca_h

        cv2.putText(frame, f"MAR: {mar:.2f}", (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if mar > LIMIAR_MAR_ABRIR and not boca_aberta:
            boca_aberta = True
            aberturas_boca += 1
            #arduino.write(b'R')

        elif mar < LIMIAR_MAR_FECHAR and boca_aberta:
            boca_aberta = False

        cv2.putText(frame, f"BOCA ABERTAS: {aberturas_boca}", (10, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Detector de Fadiga", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#arduino.close()
cv2.destroyAllWindows()
