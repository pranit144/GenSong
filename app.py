import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import urllib.parse

# Set Streamlit page configuration
st.set_page_config(
    page_title="Text-to-Music Generator 🎵",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #eaf6fb;
            color: #003366;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #4dabf5;
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #007bb5;
        }
        .stTextArea textarea {
            border: 2px solid #4dabf5;
            border-radius: 8px;
        }
        iframe {
            border: 2px solid #4dabf5;
            border-radius: 8px;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #003366;
        }
        .description {
            text-align: center;
            font-size: 18px;
            color: #005792;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize the Hugging Face model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained('sander-wood/text-to-music')
    model = AutoModelForSeq2SeqLM.from_pretrained('sander-wood/text-to-music')
    return tokenizer, model

# Load model and tokenizer
tokenizer, model = load_model()

# Streamlit App UI
st.markdown("<div class='title'>🎵 Text-to-Music Generator 🎵</div>", unsafe_allow_html=True)
st.markdown("""
<div class='description'>
Enter a textual description, and the model will generate music in ABC notation.  
You can use tools like [abc2midi](http://abc.sourceforge.net/abcMIDI/) to convert the notation into a playable file.
</div>
""", unsafe_allow_html=True)

# Input Fields
with st.container():
    text_input = st.text_area(
        "Enter a description for the music:",
        placeholder="e.g., This is a traditional Irish dance music.",
    )
    max_length = st.slider(
        "Maximum Length of Generated Music:", min_value=128, max_value=2048, value=1024, step=128
    )
    top_p = st.slider(
        "Top-p (Nucleus Sampling):", min_value=0.1, max_value=1.0, value=0.9, step=0.05
    )
    temperature = st.slider(
        "Temperature (Sampling Diversity):", min_value=0.1, max_value=2.0, value=1.0, step=0.1
    )

# Generate Music Button
if st.button("Generate Music 🎶"):
    if not text_input.strip():
        st.error("Please enter a valid description!")
    else:
        st.info("Generating music... This might take a few seconds.")

        try:
            # Tokenize input
            input_ids = tokenizer(text_input, return_tensors='pt', truncation=True, max_length=max_length)['input_ids']

            # Generate music using efficient beam search sampling
            generated_ids = model.generate(
                input_ids,
                max_length=max_length,
                do_sample=True,
                top_p=top_p,
                temperature=temperature,
                eos_token_id=tokenizer.eos_token_id,
            )

            # Decode generated music
            tune = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
            tune = "X:1\n" + tune

            st.success("Music generated successfully!")

            # Display raw generated music in the app
            st.text_area("Generated Music (ABC Notation):", value=tune, height=300)

            # Encode tune for URL and embed ABCJS Editor
            encoded_tune = urllib.parse.quote(tune)
            editor_url = f"https://www.abcjs.net/abcjs-editor?abc={encoded_tune}"
            st.markdown(f"""
            ### ABCJS Editor Preview
            You can edit or play the music below:
            <iframe src="{editor_url}" width="100%" height="500" style="border:none;"></iframe>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
