import streamlit as st
from PIL import Image
from ocr_module import extract_text_ocr_space, extract_text_paddleocr
from ai_simplifier import simplify_instruction_with_openrouter
from speech_translate import translate_text, generate_tts

st.set_page_config(page_title="MediMorph AI", layout="centered")
st.title("🧬 MediMorph AI")
st.caption("👵 Simplifying medical instructions for elderly users")

# Upload and OCR
st.markdown("### 📸 Upload Prescription Image (Optional)")
image_file = st.file_uploader("Upload a prescription (JPG/PNG)", type=["jpg", "jpeg", "png"])

openrouter_key = st.text_input("🔐 Enter OpenRouter API Key", type="password")

language = st.selectbox("🌐 Translate to", options=["None", "Malayalam", "Hindi", "Tamil", "Telugu"], index=1)
lang_codes = {"None": None, "Malayalam": "ml", "Hindi": "hi", "Tamil": "ta", "Telugu": "te"}

input_text = ""

# ------------------- OCR DEMO MODE -------------------
if image_file:
    st.image(image_file, caption="📄 Uploaded Image", use_column_width=True)
    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text_paddleocr("mock_image_path.jpg")  # Simulated result
        st.text_area("📝 Extracted Text", value=extracted_text, height=150)
        input_text = extracted_text
elif st.button("🔍 Run OCR Demo without Image"):
    with st.spinner("🧪 Running demo OCR..."):
        extracted_text = extract_text_paddleocr("mock_image_path.jpg")
        st.text_area("📝 Demo Extracted Text", value=extracted_text, height=150, key="demo_ocr_text")
        input_text = extracted_text

# ------------------- Manual Input -------------------
manual_text = st.text_area("✍️ Or enter medical instruction manually", value=input_text or "", height=120)

# ------------------- Simplification, Translation, TTS -------------------
if st.button("🔄 Simplify Instruction"):
    if not openrouter_key.strip():
        st.warning("Enter your OpenRouter API key.")
    elif manual_text.strip():
        with st.spinner("🧠 Simplifying..."):
            simplified = simplify_instruction_with_openrouter(manual_text, openrouter_key)
            st.success("📘 Simplified Instruction:\n\n" + simplified)

            lang_code = lang_codes.get(language)
            if lang_code:
                translated = translate_text(simplified, lang_code)
                st.markdown(f"### 🌍 Translated to {language}")
                st.info(translated)

            st.markdown("### 🔊 Listen")
            audio_data = generate_tts(simplified)
            st.audio(audio_data, format="audio/mp3")
            st.download_button("⬇️ Download Audio", audio_data, file_name="medimorph_instruction.mp3")
    else:
        st.warning("Please upload or enter instructions.")

st.markdown("---")
st.caption("Built with ❤️ using OCR, AI, TTS, and Translation.")
