from flask import render_template

class Speech:
    @staticmethod
    def speak(text):
        return render_template('speech.html', text=text)
