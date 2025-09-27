import cv2
import easyocr

reader = easyocr.Reader(['en'], gpu=True)
# print("Device:", reader.device)

def detect_text_regions(img):
    results  = reader.readtext(img)
    cropped_images = []

    for (bbox, text, confidence) in results:
        top_left = tuple(map(int,bbox[0]))
        bottom_right = tuple(map(int,bbox[2]))

        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

        x1, y1 = top_left
        x2, y2 = bottom_right
        cropped = img[y1:y2, x1:x2]
        cropped_images.append(cropped)

    return cropped_images, img
