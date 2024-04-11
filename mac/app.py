import logging
import tkinter as tk
from tkinter import messagebox

from mic_service import MicService

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class App:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Mic Control")
        self.app.geometry("200x80")

        self.button_mute = tk.Button(self.app, text="Mute Mic", command=self.mute)
        self.button_unmute = tk.Button(self.app, text="Unmute Mic", command=self.unmute)

        self.button_mute.pack(pady=5)
        self.button_unmute.pack(pady=5)
        logger.info("App is ready")

    def start(self):
        logger.info("Starting App")
        self.app.mainloop()

    def mute(self):
        try:
            logger.info("Muting the mic")
            MicService.mute_mic()
            self.button_mute.config(text="Mic is muted", fg="grey")
            self.button_unmute.config(text="Unmute Mic", fg="black")
            logger.info("Mic muted")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def unmute(self):
        try:
            logger.info("Unmuting the mic")
            MicService.unmute_mic()
            self.button_mute.config(text="Mute Mic", fg="black")
            self.button_unmute.config(text="Mic is unmuted", fg="grey")
            logger.info("Mic unmuted")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


App().start()
