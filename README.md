# Тестовое задание

## Использованные технологии

- TinyDB
- Flask
- Unittest
- RegEX

## Запуск кода

1. Установить Python 3.11.4
2. Установить `pipenv`
    
    `pip install pipenv`

3. Скачать репозиторий через `git clone`
4. Установить зависимости через `pipenv install`
5. Запустить консоль виртуального окружения `pipenv shell` или выбрать его в настройках IDE
6. Запустить программу через `python main.py` или через UI IDE

## Запуск Unit-тестов

1. Проделать шаги 1-5 из [запуска кода](#запуск-кода)
2. Запустить тестирование командой `python tests.py` или запустить через IDE

## Описание работы программы

После запуска кода разворачивается небольшой веб-сервер, принимающий по адресу http://localhost:5000/get_form POST-запросы c телом в виде JSON в формате:
```json
{
    "lead_phone": "+79991234567",
    "lead_email": "email@example.com"
}
```
И отдает на них список найденных форм в формате:
```json
[
    {
        "name": "Form1"
    },
    {
        "name": "Form2"
    }
]
```
Если форма не была найдена, то отадет тип принятых данных, например:
```json
{
    "lead_phone": "phone",
    "lead_email": "email"
}
```
