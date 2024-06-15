import tkinter as tk
from tkinter import Label, Entry, Button
from langdetect import detect
from langcodes import Language
import language_data

class LanguageDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Language Detector")

        self.label = Label(master, text="Enter text:")
        self.label.pack()

        self.text_entry = Entry(master, width=40)
        self.text_entry.pack()

        self.detect_button = Button(master, text="Detect Language", command=self.detect_language)
        self.detect_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def detect_language(self):
        input_text = self.text_entry.get()

        if input_text.strip():  # Check if the input text is not empty or just whitespace
            try:
                language_code = detect(input_text)
                language_name = Language.get(language_code).display_name('en')  # Specify the language for display name
                self.result_label.config(text=f"The detected language is: {language_name}")
            except Exception as e:
                self.result_label.config(text=f"Error during language detection: {e}")
        else:
            self.result_label.config(text="Please enter some text for language detection.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageDetectorApp(root)
    root.mainloop()