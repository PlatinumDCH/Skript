import psutil


def monitor_memory():
    # Получение данных об использовании памяти
    memory_info = psutil.virtual_memory()

    print(f"Общая память: {memory_info.total / (1024 ** 3):.2f} GB")
    print(f"Используемая память: {memory_info.used / (1024 ** 3):.2f} GB")
    print(f"Свободная память: {memory_info.available / (1024 ** 3):.2f} GB")
    print(f"Процент использования памяти: {memory_info.percent}%")


if __name__ == "__main__":
    monitor_memory()