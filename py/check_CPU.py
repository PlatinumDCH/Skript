# Скрипт написан на Python
import psutil
import time


def print_system_usage(interval=1):
    print("Monitoring CPU and Memory usage. Press Ctrl+C to stop.")

    try:
        while True:
            # Получаем процент использования CPU
            cpu_usage = psutil.cpu_percent(interval=interval)
            # Получаем использование памяти
            memory_info = psutil.virtual_memory()

            # Выводим информацию о загрузке системы
            print(f"CPU Usage: {cpu_usage}%")
            print(
                f"Memory Usage: {memory_info.percent}% (Used: {memory_info.used / (1024 ** 3):.2f} GB, Total: {memory_info.total / (1024 ** 3):.2f} GB)")
            print("-" * 40)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")


if __name__ == "__main__":
    print_system_usage()