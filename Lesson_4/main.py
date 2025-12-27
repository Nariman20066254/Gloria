import json
import pyaudio
from vosk import Model, KaldiRecognizer

# ==============================
# Настройка модели Vosk
# ==============================
model = Model("Lesson_4/model_small")  # Путь к папке с моделью
recognizer = KaldiRecognizer(model, 16000)

# ==============================
# Настройка микрофона через PyAudio
# ==============================
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8000)
stream.start_stream()

print("Говорите что-нибудь... (скажите 'выход' чтобы завершить)")

# ==============================
# Основной цикл
# ==============================
while True:
    data = stream.read(8000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result.get("text", "").strip()

        if text:
            print("Распознано:", text)

            if text.lower() == "выход":
                print("Завершение программы...")
                break

# ==============================
# Очистка ресурсов
# ==============================
stream.stop_stream()
stream.close()
p.terminate()
