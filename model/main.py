import cv2
from text_detection import detect_text_regions
from utils.text_recognition import recognize_text
from utils.text_interpretation import summarize_text
from utils.file_writer import append_to_docx


def main():
    # print("Using GPU:", torch.cuda.is_available())
    # print("GPU Device:", torch.cuda.get_device_name() if torch.cuda.is_available() else "None")

    cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    while True:
        ret, img = cap.read()
        if not ret:
            break

        regions, annotated_frame = detect_text_regions(img)

        for region in regions:
            text = recognize_text(region)
            if text:
                interpreted_text = summarize_text(text)
                append_to_docx(interpreted_text)
                print(f'Text: {text} \n Interpreted Text: {interpreted_text}')

        cv2.imshow('Image', annotated_frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

