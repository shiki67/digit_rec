import io
from PIL import Image
from fastapi import APIRouter, UploadFile, File
from app.schemas import HealthResponse, RecognizeResponse
from app import model

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="ok")


@router.post("/recognize", response_model=RecognizeResponse)
async def recognize(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    digit, confidence = model.predict(image)
    return RecognizeResponse(digit=digit, confidence=confidence)
