import pyttsx3


class SayText:
    def __init__(self):
        super(SayText, self).__init__()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 50)
        self.engine.setProperty('volume', 1.0)
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.tingting')
        voices = self.engine.getProperty('voices')
        for voice in voices:
            print(voice.id, voice.languages)

    def say(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()


if __name__ == '__main__':
    say_text = SayText()
    say_text.say('恭喜Solarex答对，获得20分')
    say_text.say('恭喜HWZ答对，获得50分')
