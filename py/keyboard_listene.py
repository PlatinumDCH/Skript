# Скрипт написан на Python
from pynput import keyboard


def on_press(key):
    try:
        print(f"Key {key.char} pressed.")
    except AttributeError:
        print(f"Special key {key} pressed.")


def on_release(key):
    print(f"Key {key} released.")
    if key == keyboard.Key.esc:
        # Останавливает слушатель
        return False


# Создаем слушатель для отслеживания нажатий клавиш
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()