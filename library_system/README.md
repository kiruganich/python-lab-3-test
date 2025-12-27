# Library Management System (Laboratory Work №4)

### **Цель:** Реализовать систему управления библиотекой с пользовательскими коллекциями и псевдослучайной моделью

### **Функционал:**
- **Управление книгами:**
  - `Book` — класс книги с полями: название, автор, год, жанр, ISBN
  - `BookCollection` — пользовательская списковая коллекция для хранения книг
  - `IndexDict` — пользовательская словарная коллекция для индексации книг по ISBN, автору и году
- **Поиск книг:**
  - Поиск по автору, жанру, году, ISBN
  - Использование индексов для эффективного поиска
- **Библиотека:**
  - `Library` — основной класс библиотеки с коллекцией книг и индексами
  - Методы добавления/удаления/поиска книг
- **Псевдослучайная симуляция:**
  - Симуляция работы библиотеки с 5+ различными событиями
  - Воспроизводимые результаты с использованием seed
- **Дополнительный функционал:**
  - Поддержка логирования всех операций
  - Пользовательские коллекции с поддержкой итерации, индексации, срезов
  - Наследование и абстрактные классы
  - Магические методы (__getitem__, __iter__, __len__, __call__, __repr__)

## Структура проекта

```
library_system/
│
├── src/
│   ├── constants.py                 # Константы для симуляции
│   ├── book.py                      # Класс Book
│   ├── book_collection.py           # Списковая коллекция книг
│   ├── index_dict.py                # Словарная коллекция индексов
│   ├── library_base.py              # Базовый класс LibraryItem
│   ├── library.py                   # Основной класс Library
│   └── simulation.py                # Модуль симуляции
├── tests/
│   └── test.py                      # Тесты для всех компонентов
├── .gitignore                       # Файл для игнорирования файлов Git
├── main.py                          # Точка входа
├── README.md                        # Описание проекта
└── requirements.txt                 # Зависимости проекта
```


![image](image.png)


## Установка

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/library_system.git 
cd library_system
```

### 2. Установите зависимости:

```bash
pip install -r requirements.txt
```

### 3. Запустите программу:

```bash
python main.py
```

Дополнительные параметры:
- `--steps N` — количество шагов симуляции (по умолчанию 20)
- `--seed N` — значение seed для воспроизводимости (необязательно)

Примеры:
```bash
python main.py --steps 30
python main.py --steps 10 --seed 123
```

## Примеры работы
```bash
Starting Library Management System Simulation...
Running simulation with 20 steps
--------------------------------------------------
Added book: The Great Adventure by John Smith
Added book: Mystery of the Old House by Emily Johnson
Searched for author 'Emily Johnson', found 1 books
Updated library indices
Added book: Echoes of Time by Lisa Martinez
Searched for year 1987, found 0 books
No books to remove
...

Simulation completed!
Final library status: Library 'Simulation Library' contains 12 books
Total unique authors: 10
```

## Зависимости

```
Python 3.8+
pytest>=7.0.0
```