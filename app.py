import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translator")  

# User Input
text = st.text_area("Enter text to translate:")

# Language Selection
source_lang = st.selectbox("Select Source Language", ["auto", "hi", "bn", "ta", "te", "mr", "gu", "ml", "kn", "pa", "or", "ur"])
target_lang = "en"  # English (You can modify this)

# Translate Button
if st.button("Translate"):
    if text.strip():
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        st.success(f"**Translated Text:** {translated_text}")
    else:
        st.warning("⚠️ Please enter text to translate.")

st.write("💡 Supports multiple Indian languages and Urdu!")
