import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Load the pre-trained MobileNet SSD model and the prototxt file
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'mobilenet_iter_73000.caffemodel')

# Function to send an email alert
def send_email_alert(frame):
    email_user = 'youremail@example.com'
    email_password = 'yourpassword'
    email_send = 'recipient@example.com'
    subject = 'Person Detected!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'A person has been detected in your home.'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'person_detected.jpg'
    cv2.imwrite(filename, frame)

    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, email_send, text)
    server.quit()

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the frame for object detection
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])

            # Check if the detected object is a person (class label 15 for COCO dataset)
            if idx == 15:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # Draw bounding box around the person
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                
                # Send email alert
                send_email_alert(frame)
                break

    cv2.imshow('Frame', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
