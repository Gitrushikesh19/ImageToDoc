import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def recognize_text(region):

    results = reader.readtext(region)
    full_text = ' '.join([result[1] for result in results])
    return full_text.strip()
