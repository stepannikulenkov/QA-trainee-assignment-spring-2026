# Инструкция по запуску тестов.

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

### Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале:
```bash
git clone <https://github.com/stepannikulenkov/QA-trainee-assignment-spring-2026.git>
```
### Перейдите в директорию проекта
```bash
cd QA-trainee-assignment-spring-2026
```
### Создайте виртуальное окружение и установите зависимости
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\\Scripts\\activate    # Windows
```
### Установите зависимости
```bash
pip install -r requirements.txt
```

### Запустите все тесты
```bash
pytest
```

### Или запустите с подробным выводом
```bash
pytest -v
```
