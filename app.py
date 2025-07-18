import streamlit as st
from PIL import Image
from ocr_module import extract_text_ocr_space, extract_text_paddleocr
from ai_simplifier import simplify_instruction_with_openrouter
from speech_translate import translate_text, generate_tts

st.set_page_config(page_title="MediMorph AI", layout="centered")
st.title("🧬 MediMorph AI")
st.caption("👵 Simplifying medical instructions for elderly users")

# --- Inputs ---
openrouter_key = st.text_input("🔐 Enter OpenRouter API Key (optional)", type="password")
language = st.selectbox("🌐 Translate to", options=["None", "Malayalam", "Hindi", "Tamil", "Telugu"], index=1)
lang_codes = {"None": None, "Malayalam": "ml", "Hindi": "hi", "Tamil": "ta", "Telugu": "te"}

# --- OCR Image Upload ---
st.markdown("### 📸 Upload Prescription Image (Optional)")
image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
input_text = ""

if image_file:
    st.image(image_file, caption="📄 Uploaded Image", use_container_width=True)
    with st.spinner("🔍 Extracting text from image..."):
        extracted_text = extract_text_paddleocr("mock_image_path.jpg")  # This will be replaced by your friend's module
        input_text = extracted_text
        st.text_area("📝 Extracted Text", value=extracted_text, height=150, key="uploaded_text")

elif st.button("🧪 Run Demo Without Upload"):
    with st.spinner("Extracting demo text..."):
        demo_text = extract_text_paddleocr("mock_image_path.jpg")
        input_text = demo_text
        st.text_area("📝 Demo Extracted Text", value=demo_text, height=150, key="demo_text")

# Manual Input Section
manual_text = st.text_area("✍️ Or enter medical instruction manually", value=input_text or "", height=120)

# --- Simplify Button ---
if st.button("🔄 Simplify Instruction"):
    if not manual_text.strip():
        st.warning("⚠️ Please upload an image or enter some text.")
    else:
        with st.spinner("🧠 Simplifying using AI..."):
            simplified = simplify_instruction_with_openrouter(manual_text, openrouter_key or None)
            st.success("📘 Simplified Instruction")
            st.markdown(simplified)

        # --- Translation ---
        lang_code = lang_codes.get(language)
        if lang_code:
            with st.spinner("🌍 Translating..."):
                translated = translate_text(simplified, lang_code)
                st.markdown(f"### 🌐 Translated to {language}")
                st.info(translated)
        else:
            translated = simplified  # No translation

        # --- TTS ---
        with st.spinner("🔊 Generating audio..."):
            audio_data = generate_tts(translated)
            st.audio(audio_data, format="audio/mp3")
            st.download_button("⬇️ Download Audio", audio_data, file_name="medimorph_instruction.mp3")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using OCR, AI, TTS, and Translation.")
