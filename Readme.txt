Text-to-Music Generator 🎵

Overview

Welcome to the Text-to-Music Generator! This app allows you to input a textual description and generates music in ABC notation using a Hugging Face model. You can then edit or play the generated music using an embedded ABCJS editor.



Features

🎨 Intuitive Interface: A clean and user-friendly UI for entering textual descriptions.

🎶 Music Generation: Converts your text into music using a pre-trained Hugging Face model.

✨ ABC Notation Support: Displays the generated music in ABC notation, which can be easily converted to MIDI.

🎵 ABCJS Editor: Embedded editor for viewing, editing, and playing your music.

🌈 Custom Styling: Enhanced with animations and transitions for a visually appealing experience.

Setup and Installation

Clone the Repository:

git clone https://github.com/your-username/text-to-music-generator.git
cd text-to-music-generator

Install Dependencies:

pip install -r requirements.txt

Run the App:

streamlit run app.py

Access the App:
Open your web browser and go to http://localhost:8501.

Usage

Enter a Description: Provide a textual description of the music you want to generate (e.g., "A cheerful Irish jig").

Adjust Parameters:

Maximum Length: Control the length of the generated music.

Top-p: Adjust the nucleus sampling for creativity.

Temperature: Change the diversity of the output.

Generate Music: Click the "Generate Music 🎶" button.

View and Edit: The generated music will appear in ABC notation. Use the embedded editor to modify or play it.

Animation and Transition Enhancements

To add animations and transitions to the app:

CSS for Animations

Add this CSS block to the Streamlit app for smooth transitions and hover effects:

<style>
    body {
        animation: fadeIn 2s;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .stButton>button {
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #007bb5;
        transform: scale(1.05);
    }
</style>

Model Details

Model: sander-wood/text-to-music

Tokenization: Utilizes AutoTokenizer for preparing text input.

Generation: Uses beam search sampling to generate diverse musical outputs.

How It Works

Input Processing: The description is tokenized using the Hugging Face AutoTokenizer.

Music Generation: The model generates ABC notation from the input tokens.

Output Rendering: The generated notation is displayed and editable in the ABCJS editor.

Contributing

Contributions are welcome! Please open an issue or submit a pull request to improve the app.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

For questions or feedback, feel free to reach out:

Email: your-email@example.com

GitHub: Your GitHub Profile

Enjoy creating music with text! 🎵
