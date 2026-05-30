# Digit Recognizer API

Процесс выбора модели можно увидеть по ссылке https://colab.research.google.com/drive/1gEhTvTsJcfYSMe4WgIrZLCbPf-zKdbKM?usp=sharing

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

