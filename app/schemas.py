from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class RecognizeResponse(BaseModel):
    digit: int
    confidence: float
