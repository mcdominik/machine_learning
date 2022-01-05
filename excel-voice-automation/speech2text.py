import speech_recognition as sr


class Speech2text:
    def __init__(self, recognizer=sr.Recognizer(), source=sr.Microphone(), ambient_adjust=False):
        self.recognizer = recognizer
        self.source = source
        self.ambient_adjust = ambient_adjust

    def listen(self):
        with self.source as source:
            print("listening...")
            if self.ambient_adjust == True:
                self.recognizer.adjust_for_ambient_noise(source)
            else:
                pass
            audio_text = self.recognizer.listen(source)
            print("Time over, thanks")
        #recoginize_() method will throw a request error if the API is unreachable
        try:
            # using google speech recognition (several others available)
            result = self.recognizer.recognize_google(audio_text)
            print("Text: "+ result)
            return result
        except:
            print("Sorry, I did not get that")

    def audio_file(self, audio_path):
        self.source = sr.AudioFile(audio_path)
        with self.source as source:
            sample = self.recognizer.record(source)
        print(self.recognizer.recognize_google(sample))


