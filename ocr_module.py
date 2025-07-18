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

# PaddleOCR integration (mock version, your friend will update this)
def extract_text_paddleocr(image_path):
    # Replace this with actual PaddleOCR code
    return "Mocked output from PaddleOCR"
