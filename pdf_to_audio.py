from tkinter import *
import tkinter.messagebox as msgb
from tkinter import filedialog
import subprocess

import PyPDF2
from gtts import gTTS

import os
import shutil


TITLE_FONT = "Arial"
TITLE = "#00ADB5"
WORD_FONT = "Times New Roman"
WORD = "#EEEEEE"
BACKGROUND = "#222831"

root = Tk()
root.title("Pdf to Audio")
root.config(padx=25, pady=25, bg=BACKGROUND)


def create_directory_if_not_exists(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        # If it doesn't exist, create it
        os.makedirs(directory_path)

def close_the_app():
    if msgb.askokcancel("Quit", "Do you want to close the app? Make sure that you downloaded the Watermarked Image"):
        root.destroy()

def select_pdf():
    filename = filedialog.askopenfilename(initialdir='/Downloads', title='Select image', filetypes=(('PDF files', '*.pdf'), ('All files', '*.*')))

    if filename:

        save_directory = 'uploaded_pdf'  # Replace this with the desired directory path
        create_directory_if_not_exists(save_directory)
        
        # Move the selected PDF file to the 'uploaded_pdf' directory
        pdf_path = os.path.join(save_directory, 'file.pdf')
        shutil.copy(filename, pdf_path)

        # Now, you can open the moved PDF file
        pdf_file = open(pdf_path , 'rb')
        pdfreader = PyPDF2.PdfReader(pdf_file)

        all_text = ''
        for page_num in range(len(pdfreader.pages)):
            text = pdfreader.pages[page_num].extract_text()
            clean_text = text.strip().replace('\n',' ')
            all_text += clean_text
        pdf_file.close()

        audio_directory = 'audios'  # Replace this with the desired directory path
        create_directory_if_not_exists(audio_directory)

        tts = gTTS(all_text)
        tts.save('audios/audio.mp3')
        play_btn.pack()
        download_btn.pack()
        close_btn.pack()
        
    else:
        # Handle the case where the user canceled the file dialog
        msgb.showerror('No file was chosen , please choose a file')


def play_audio():
    audio_file_path = 'audios/audio.mp3'
    subprocess.call(['open', audio_file_path])

def download_audio():
    # Ask the user to choose the download location and filename
    download_path = filedialog.asksaveasfilename(initialdir="/", title="Save Audio As", defaultextension=".mp3", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))

    # If the user canceled the download or didn't choose a location, return without doing anything
    if not download_path:
        return

    # Check if the chosen file already exists, and if it does, ask the user for confirmation to overwrite it
    if os.path.exists(download_path):
        if not msgb.askokcancel("Warning", "File already exists. Do you want to overwrite it?"):
            return

    # Copy the image file to the chosen download location
    try:
        audio_path = os.path.join('audios', 'audio.mp3')
        shutil.copy(audio_path, download_path)
        msgb.showinfo("Success", "Image downloaded successfully!")
    except Exception as e:
        msgb.showerror("Error", f"Failed to download audio: {e}")


title_label = Label(text="PDF To Audio", font=(TITLE_FONT, 54, "bold"), fg=TITLE, bg=BACKGROUND)
title_label.pack()

upload_btn = Button(text='Select PDF', font=(WORD_FONT, 35), fg='black', bg=BACKGROUND,padx=10,pady=5, command=select_pdf)
upload_btn.pack()

play_btn = Button(text='Play Audio', font=(WORD_FONT, 35), fg='black', bg=BACKGROUND,padx=10,pady=5,command=play_audio)

close_btn = Button(text='Close App', font=(WORD_FONT, 35), fg='black', bg=BACKGROUND,padx=10,pady=5,command=close_the_app)

download_btn = Button(text='Download Audio', font=(WORD_FONT, 35), fg='black', bg=BACKGROUND,padx=10,pady=5,command=download_audio)


root.mainloop()
