import cv2

xml_haar_cascade = 'haarcascade_frontalface_alt2.xml'

# Função de números de faces detectadas com opencv
def funcao_numero_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassifier.detectMultiScale(gray)
    return len(faces)

# Carrega o classificador
faceClassifier = cv2.CascadeClassifier(xml_haar_cascade)

# Iniciar camera
capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)

while not cv2.waitKey(20) & 0xFF == ord("q"):
    # Captura frame
    ret, frame_color = capture.read()

    # Converte para escala de cinza
    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)

    faces = faceClassifier.detectMultiScale(gray)

    for x, y, w, h in faces:
        cv2.rectangle(frame_color, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('color', frame_color)

    print(funcao_numero_faces(frame_color))


