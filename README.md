
# Language-Translation-App

## Description
This project is a language translation application built using Streamlit and the Helsinki-NLP/Opus-MT models from Hugging Face's transformers library. The app supports translation between multiple languages and leverages open-source machine translation models to provide accurate and efficient translations.

## Features
- Translate text between a variety of languages, including English, French, German, Spanish, Italian, Portuguese, Russian, Chinese, Japanese, and Arabic.
- User-friendly interface with language selection and text area for input.
- Real-time translation using pre-trained machine translation models.
- Supports efficient caching of models to optimize performance.

## Model Details
- Helsinki-NLP/Opus-MT models are pre-trained machine translation models.
- The models are fine-tuned versions of MarianMT, a highly efficient neural machine translation architecture.
- Each model is specific to a language pair (e.g., English to French, French to German).
- MarianMT models are lightweight and designed for real-world applications, making them an ideal choice for this app.

## Project Workflow
- Language Selection: Users select the source and target languages from a dropdown menu.
- Input Text: Users enter the text they want to translate in the provided text area.
- Translation: The app loads the corresponding translation model using Hugging Face's MarianMTModel and MarianTokenizer. The text is tokenized, translated, and decoded to produce the output.
- Output Display: The translated text is displayed below the input area.

## Technology Stack
- Frontend: Streamlit for the interactive user interface.
- Backend: Hugging Face's transformers library for loading and using pre-trained models.
- Programming Language: Python


## Installation

- Clone the repository:

```http
git clone https://github.com/muhammadtalha72014/Language-Translation-App.git  
cd Language-Translation-App  
```
- Install the required dependencies:

```http
pip install -r requirements.txt
```
- Run the application:

```http
streamlit run app.py  
```
## Output

![Screenshot 2024-12-20 165012](https://github.com/user-attachments/assets/7c83ec2e-dcd3-48de-aa1d-5b4e33877ec2)

## Acknowledgements

 - Helsinki-NLP: For providing open-source machine translation models.
 - Streamlit: For enabling rapid and interactive app development

Let me know if you’d like any additional details or modifications!
