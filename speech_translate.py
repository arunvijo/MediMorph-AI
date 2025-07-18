import pyttsx3
import tempfile
from googletrans import Translator

translator = Translator()

def translate_text(text, target_lang='ml'):
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"❌ Translation failed: {e}"

def generate_tts(text):
    engine = pyttsx3.init()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        engine.save_to_file(text, fp.name)
        engine.runAndWait()
        with open(fp.name, 'rb') as f:
            return f.read()
