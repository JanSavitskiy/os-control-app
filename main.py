from tkinter import *
import psutil
import platform

def get_size(bytes, suffix="B"):
    """Convert bytes to a more readable format."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor


def update_info():
    """Update system information in the text area."""
    # Получаем данные о системе
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_total = get_size(memory.total)
    memory_available = get_size(memory.available)
    memory_used = get_size(memory.used)
    memory_percentage = memory.percent

    # Получаем информацию о системе
    system_info = platform.uname()
    system_name = system_info.system
    node_name = system_info.node
    release = system_info.release
    version = system_info.version
    machine = system_info.machine
    processor = system_info.processor

    # Формируем вывод
    info_text = f"Система: {system_name}\n"
    info_text += f"Имя узла: {node_name}\n"
    info_text += f"Версия: {release}\n"
    info_text += f"Архитектура: {machine}\n"
    info_text += f"Процессор: {processor}\n"
    info_text += f"Использование CPU: {cpu_usage}%\n"
    info_text += f"Общая память: {memory_total}\n"
    info_text += f"Доступная память: {memory_available}\n"
    info_text += f"Используемая память: {memory_used}\n"
    info_text += f"Процент использования памяти: {memory_percentage}%\n"

    # Обновляем текстовое поле
    text_area.delete(1.0, END)  # Очищаем текстовое поле
    text_area.insert(END, info_text)  # Вставляем новое содержание


# Создаем главное окно
root = Tk()
root.title('Анализатор ОС')
root.geometry("600x600")

# Создаем текстовое поле для отображения информации
text_area = Text(root, wrap='word', font=("Courier New", 10))
text_area.pack(expand=True, fill='both')

# Кнопка для обновления информации
update_button = Button(root, text="Обновить информацию", command=update_info)
update_button.pack(pady=10)

# Обновляем информацию при запуске
update_info()

# Запускаем главный цикл
root.mainloop()
