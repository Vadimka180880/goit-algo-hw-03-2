import os
import shutil
import argparse

def copy_files_recursively(src, dest):
    """
    Рекурсивно копіює файли з вихідної директорії до директорії призначення, сортує їх за розширенням файлів.
    
    src: шлях до вихідної директорії
    dest: шлях до директорії призначення
    """
    # Якщо директорія призначення не існує, створюємо її
    if not os.path.exists(dest):
        os.makedirs(dest)

    # Перебираємо всі елементи у вихідній директорії
    for item in os.listdir(src):
        s = os.path.join(src, item)
        # Якщо елемент є директорією, викликаємо функцію рекурсивно
        if os.path.isdir(s):
            copy_files_recursively(s, dest)
        else:
            # Визначаємо розширення файлу
            file_extension = os.path.splitext(item)[1][1:]
            extension_dir = os.path.join(dest, file_extension)
            # Якщо директорія для розширення не існує, створюємо її
            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)
            # Копіюємо файл у відповідну директорію
            shutil.copy2(s, extension_dir)

def main():
    import sys
    print("Running script with the following arguments:")
    print(sys.argv)
    
    # Парсер для аргументів командного рядка
    parser = argparse.ArgumentParser(description='Copy files recursively and sort them by extension.')
    parser.add_argument('source', type=str, help='Path to the source directory')  # Вхідний аргумент - шлях до вихідної директорії
    parser.add_argument('destination', nargs='?', default='dist', type=str, help='Path to the destination directory (default: dist)')  # Вхідний аргумент - шлях до директорії призначення (за замовчуванням dist)

    args = parser.parse_args()
    print(f"Source directory: {args.source}")
    print(f"Destination directory: {args.destination}")
    
    source_directory = args.source
    destination_directory = args.destination

    # Перевірка наявності вихідної директорії
    if not os.path.exists(source_directory):
        print(f"Source directory '{source_directory}' does not exist.")
        return

    # Виведення вмісту вихідної директорії
    print(f"Contents of source directory '{source_directory}':")
    print(os.listdir(source_directory))
    
    try:
        # Рекурсивне копіювання файлів
        copy_files_recursively(source_directory, destination_directory)
        print(f"Files have been copied and sorted to '{destination_directory}'")
    except Exception as e:
        # Обробка винятків
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Виведення місцезнаходження файлу скрипта
    print(f"Script file location: {os.path.abspath(__file__)}")
    main()

