# Digit Recognizer API

## Запуск

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Эндпоинты

Проверяет работает ли сервер
`GET /health` → `{"status": "ok"}`

Распознает цифру по изображению и возвращает цифру и степень уверенности
`POST /recognize` - поле `file` (PNG/JPEG) → `{"digit": 3, "confidence": 0.97}`

