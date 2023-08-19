import json
import os
from datetime import datetime

# Функция для создания новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes()

# Функция для сохранения заметок в JSON файле
def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

# Функция для чтения списка заметок
def read_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Дата/время: {note['timestamp']}")
        print(f"Текст: {note['body']}\n")

# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с таким ID не найдена.")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена.")
            return
    print("Заметка с таким ID не найдена.")
    
def find_note_by_id(note_id):
    for note in notes:
        if note["id"] == note_id:
            print(f"Заметка найдена (ID: {note['id']}):")
            print(f"Заголовок: {note['title']}")
            print(f"Дата/время: {note['timestamp']}")
            print(f"Текст: {note['body']}\n")
            return
    print("Заметка с таким ID не найдена.")

# Функция для поиска заметки по заголовку
def find_note_by_title(title):
    found_notes = []
    for note in notes:
        if title.lower() in note["title"].lower():
            found_notes.append(note)
    if found_notes:
        print("Найдены следующие заметки по заголовку:")
        for note in found_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Дата/время: {note['timestamp']}")
            print(f"Текст: {note['body']}\n")
    else:
        print("Заметки с таким заголовком не найдены.")

# Функция для поиска заметки по дате
def find_note_by_date(date):
    found_notes = []
    for note in notes:
        if date in note["timestamp"]:
            found_notes.append(note)
    if found_notes:
        print("Найдены следующие заметки по дате:")
        for note in found_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Дата/время: {note['timestamp']}")
            print(f"Текст: {note['body']}\n")
    else:
        print("Заметки с такой датой не найдены.")

# Главная функция приложения
def main():
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
    else:
        notes = []

    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Найти заметку по идентификатору")
        print("6. Найти заметку по заголовку")
        print("7. Найти заметку по дате")
        print("8. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            note_id = int(input("Введите ID заметки для поиска: "))
            find_note_by_id(note_id)
        elif choice == "6":
            title = input("Введите заголовок для поиска: ")
            find_note_by_title(title)
        elif choice == "7":
            date = input("Введите дату для поиска (гггг-мм-дд): ")
            find_note_by_date(date)
        elif choice == "8":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
