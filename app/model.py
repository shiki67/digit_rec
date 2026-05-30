import joblib
import numpy as np
from PIL import Image
from app.config import MODEL_PATH

_model = None


def get_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model


def predict(image: Image.Image) -> tuple[int, float]:
    img = image.convert("L").resize((8, 8))
    X = np.array(img, dtype=np.float32).flatten().reshape(1, -1)
    model = get_model()
    digit = int(model.predict(X)[0])
    confidence = float(model.predict_proba(X)[0][digit])
    return digit, confidence
