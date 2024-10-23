import cv2
import numpy as np
from PIL import Image
import io
import base64
import dlib

def detect_faces(image):
    # 轉換 PIL 圖片為 OpenCV 格式
    cv_image = np.array(image)

    # 使用 Dlib 偵測人臉
    detector = dlib.get_frontal_face_detector()
    
    # 將圖片轉為灰階
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    
    # 偵測人臉
    faces = detector(gray)
    
    # 在臉部位置畫框
    # 在臉部位置畫框
    detected_faces = []
    for face in faces:
        x, y, w, h = (face.left(), face.top(), face.right() - face.left(), face.bottom() - face.top())
        cv2.rectangle(cv_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        detected_faces.append({'left': x, 'top': y, 'right': face.right(), 'bottom': face.bottom()})


    # 將處理後的圖片轉換回 PIL 格式
    processed_image = Image.fromarray(cv_image)

    # 將處理後的圖片轉為 Base64 字符串
    buffered = io.BytesIO()

    # 確保轉換為 RGB 並保存為 JPEG
    if processed_image.mode == "RGBA":
        processed_image = processed_image.convert("RGB")


    processed_image.save(buffered, format="JPEG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return detected_faces, encoded_image
