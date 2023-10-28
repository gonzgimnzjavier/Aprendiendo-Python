import sounddevice as sd
import speech_recognition as sr
from gtts import gTTS
import pygame
import numpy as np
import wave
import nltk
from nltk.chat.util import Chat, reflections

# Función para grabar audio
def record_audio_from_mic():
    sample_rate = 44100
    duration = 5  # segundos
    print("Recording...")
    my_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    print("Recording finished")
    return my_data, sample_rate


# Función para guardar audio en un archivo WAV
def save_audio_to_wav(data, sample_rate, filename="output.wav"):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Aquí cambiamos a 1 canal
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())


# Función para reconocer el habla del archivo WAV
def recognize_speech_from_wav(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="es-ES")
        return text

# Función para obtener respuesta del chatbot NLTK
def get_response_from_nltk_chatbot(text):
    pairs = [
        [
            r"(.*)hola(.*)",
            ["¡Hola! ¿Cómo puedo ayudarte?", "¡Hola! ¿Qué tal?"]
        ],
        [
            r"(.*)tu nombre(.*)",
            ["Soy un bot. ¿En qué puedo ayudarte?", "Me llaman ChatGPT basado en NLTK."]
        ],
        [
            r"adiós",
            ["¡Hasta luego!", "¡Adiós!"]
        ],
        [
            r"(.*)",
            ["No entendí eso.", "¿Podrías reformularlo?"]
        ],
    ]

    chat = Chat(pairs, reflections)
    return chat.respond(text)

# Función para convertir texto a voz y reproducirlo
def speak_text(text):
    tts = gTTS(text=text, lang='es')
    filename = "temp_audio.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def main():
    # Grabar audio del micrófono
    audio_data, sample_rate = record_audio_from_mic()

    # Guardar el audio en un archivo WAV
    filename = "temp_recording.wav"
    save_audio_to_wav(audio_data, sample_rate, filename)

    # Reconocer el habla del archivo WAV
    try:
        user_speech = recognize_speech_from_wav(filename)
        print(f"Entendí: {user_speech}")

        # Obtener respuesta del chatbot NLTK
        response = get_response_from_nltk_chatbot(user_speech)

        # Reproducir la respuesta
        speak_text(response)

    except sr.UnknownValueError:
        print("Lo siento, no pude entender el audio.")

if __name__ == "__main__":
    main()
