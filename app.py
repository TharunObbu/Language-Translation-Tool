import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

# Streamlit UI
st.title("🌍 CodeAlpha Translation Tool")
st.write("Translate text into different languages and listen to the audio!")

# Input text
text = st.text_area("Enter text to translate:")

# Select target language
languages = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
    "Telugu": "te"
}
lang_choice = st.selectbox("Select language:", list(languages.keys()))

# Translate
if st.button("Translate"):
    if text.strip() != "":
        translator = Translator()
        translated = translator.translate(text, dest=languages[lang_choice])
        st.success(f"**Translated ({lang_choice}):** {translated.text}")

        # Text-to-Speech
        tts = gTTS(translated.text, lang=languages[lang_choice])
        tts.save("translated_audio.mp3")
        audio_file = open("translated_audio.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
    else:
        st.warning("⚠️ Please enter some text.")

