import pyttsx3
import tempfile
from googletrans import Translator

# Initialize the translator
translator = Translator()

def translate_text(text, target_lang='ml'):
    """
    Translate text to the target language using Google Translate.
    """
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"❌ Translation failed: {str(e)}"


def generate_tts(text):
    """
    Generate TTS audio using pyttsx3 and return the MP3 binary.
    """
    try:
        engine = pyttsx3.init()
        
        # Optional: Set voice if available
        voices = engine.getProperty('voices')
        for voice in voices:
            if "female" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break  # Use first female voice found

        # Set speech rate (optional)
        engine.setProperty('rate', 150)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            engine.save_to_file(text, fp.name)
            engine.runAndWait()
            with open(fp.name, 'rb') as f:
                return f.read()

    except Exception as e:
        print(f"❌ TTS failed: {e}")
        return None
