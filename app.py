import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Specified different languages
LANGUAGES = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
}

# Helper function to load the model and tokenizer
@st.cache_resource
def load_translation_model(src_lang, tgt_lang):  # Corrected parameter names
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"  # Corrected typo in model_name
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Translation function
def translate_text(tokenizer, model, text):
    inputs = tokenizer(text, return_tensors='pt', padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Streamlit App
st.title("Language Translation APP 🌍")
st.write("Translate text between multiple languages using open-source models.")

# Language selection
col1, col2 = st.columns(2)
with col1:
    source_language = st.selectbox("Select Source Language 🌐", list(LANGUAGES.keys()))
with col2:
    target_language = st.selectbox("Select Target Language 🌍", list(LANGUAGES.keys()))

# Input Text
text_to_translate = st.text_area("Enter text to translate", height=150)

# Translate button
if st.button("Translate"):
    if source_language == target_language:
        st.warning("Source and target language must be different")
    elif not text_to_translate.strip():
        st.warning("Please enter some text to translate")
    else:
        src_lang = LANGUAGES[source_language]
        tgt_lang = LANGUAGES[target_language]

        try:
            # Load model and tokenizer
            tokenizer, model = load_translation_model(src_lang, tgt_lang)

            # Perform translation
            translated_text = translate_text(tokenizer, model, text_to_translate)

            # Display result
            st.subheader("Translated Text 🔄:")
            st.write(translated_text)

        except Exception as e:
            st.error(f"Error: {str(e)}")
