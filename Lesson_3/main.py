from silero_tts.silero_tts import SileroTTS
import pygame 
import os


def say(text):
    name_waw = 'output.wav' 

    tts = SileroTTS(
        language='ru',
        model_id='v4_ru',
        speaker='baya'
    )

    tts.tts(text, f'{name_waw}')
    print(f"{text}✅")
    muc(f'{name_waw}')

def muc(file_name):
    """
    Проигрывает аудиофайл и удаляет его после завершения.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # уменьшает нагрузку на CPU

        pygame.mixer.music.stop()        # ⛔ Остановить
        pygame.mixer.quit()              # 🧹 Освободить ресурс

        os.remove(file_name)             # ✅ Удалить после выгрузки
    except Exception as e:
        print(f'Ошибка в функции play_music: {e}')


say('Привет меня зовут нариман ')