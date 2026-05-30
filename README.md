# Digit Recognizer API

## Структура

```
├── main.py              # точка входа
├── model.pkl            # обученная модель
├── requirements.txt
└── app/
    ├── config.py        # настройки
    ├── main.py          # фабрика FastAPI
    ├── router.py        # эндпоинты
    ├── schemas.py       # Pydantic-модели
    └── model.py         # загрузка модели и инференс
```

## Запуск

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Эндпоинты

`GET /health` → `{"status": "ok"}`

`POST /recognize` — поле `file` (PNG/JPEG) → `{"digit": 3, "confidence": 0.97}`

```bash
curl -X POST http://localhost:8000/recognize -F "file=@digit.png"
```
