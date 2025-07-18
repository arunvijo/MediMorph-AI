import requests

# OCR.Space as fallback
def extract_text_ocr_space(image_file, api_key="helloworld"):
    payload = {
        'isOverlayRequired': False,
        'apikey': api_key,
        'language': 'eng',
    }
    files = {'file': image_file}
    response = requests.post('https://api.ocr.space/parse/image', files=files, data=payload)
    try:
        result = response.json()
        return result['ParsedResults'][0]['ParsedText']
    except:
        return "⚠️ OCR failed or unreadable image."

# PaddleOCR integration (mock version, temporary)
def extract_text_paddleocr(image_path):
    # Simulated extracted text from a prescription image
    return """
Take one tablet of Paracetamol 500mg after food in the morning.
Take one capsule of Omeprazole 20mg before breakfast daily.
Apply ointment twice daily on affected area.
"""  # You can change this for other tests
