
# PDF to Audio Converter

This is a Python application that converts PDF files into audio files (MP3 format). It utilizes the PyPDF2 library to extract text from PDFs and the gTTS library to convert text to speech.(Please make be aware that the play button in the app will only be able to work for Mac OS )

## How to Use

1. Clone or download this repository to your local machine.

2. Install the required Python libraries if you haven't already. You can use pip to install them:

   ```bash
   pip3 install PyPDF2 gTTS
   ```

3. Run the `pdf_to_audio.py` script:

   ```bash
   python pdf_to_audio.py
   ```

4. Click the "Select PDF" button to choose a PDF file for conversion.

5. After selecting a PDF,it will take some time for the app to convert text into autio file .Then  you can click the "Play Audio" button to listen to the converted audio or the "Download Audio" button to save it to your computer.

6. To close the application, click the "Close App" button.

## Dependencies

- Python 3.x
- PyPDF2 library
- gTTS (Google Text-to-Speech) library

## Directory Structure

- `pdf_to_audio.py`: The main Python script.
  
  Do not worry about the following items; if you don't have them, they will be created automatically
- `uploaded_pdf/`: Directory where the selected PDF is temporarily stored.do not worry if you do not have any then they will be created automatically
- `audios/`: Directory where the converted audio file is saved.

## Note

- Make sure to have an active internet connection for the text-to-speech conversion to work, as gTTS relies on online services.

