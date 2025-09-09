import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.title("🌍 Language Translation Tool")

# User input
text = st.text_area("Enter text to translate:")
source_lang = st.text_input("Source language (e.g., 'en' for English):", "en")
target_lang = st.text_input("Target language (e.g., 'fr' for French):", "fr")

if st.button("Translate"):
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        st.success(f"**Translated Text:** {translated}")

        # Optional: Convert to speech
        tts = gTTS(translated, lang=target_lang)
        tts.save("output.mp3")
        audio_file = open("output.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")

    except Exception as e:
        st.error(f"Error: {str(e)}")
