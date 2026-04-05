Инструкция по запуску тестов.

## Структура проекта

```
├── README.md
├── Task1
│   ├── BUGS_FROM_SCREENSHOT.md
│   └── img
├── Task2
│   ├── BUGS.md
│   ├── TESTCASES.md
│   ├── TESTS
│   ├── conftest.py
│   └── utils
├── project_tree.txt
├── requirements.txt
```

## Требования

* Python 3.10+
* pip

## Установка и запуск

```bash
Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале:

git clone <https://github.com/stepannikulenkov/QA-trainee-assignment-spring-2026.git>

cd QA-trainee-assignment-spring-2026

# 2. Создайте виртуальное окружение и установите зависимости
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\\Scripts\\activate    # Windows
pip install -r requirements.txt

# 3. Запустить все тесты
pytest

# 4. Запустить с подробным выводом
pytest -v

```