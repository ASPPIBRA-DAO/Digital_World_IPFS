# instalação: SpeechRecognition e PyAudio
# para pyaudio, digite no google "install pyaudio seu_sistema_operacional"

import speech_recognition as sr

rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())
with sr.Microphone(3) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)