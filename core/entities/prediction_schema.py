from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from utils.date import get_now


class PredictionFeatures(BaseModel):
    N_Days: int = Field(...)
    Drug: str = Field(...)
    Age: int = Field(...)
    Sex: str = Field(...)
    Ascites: str = Field(...)
    Hepatomegaly: str = Field(...)
    Spiders: str = Field(...)
    Edema: str = Field(...)
    Bilirubin: float = Field(...)
    Cholesterol: float = Field(...)
    Albumin: float = Field(...)
    Copper: float = Field(...)
    Alk_Phos: float = Field(...)
    SGOT: float = Field(...)
    Tryglicerides: float = Field(...)
    Platelets: float = Field(...)
    Prothrombin: float = Field(...)
    Stage: int = Field(...)


class PredictionTarget(BaseModel):
    answer: int = Field(...)


class PredictionInfo(BaseModel):
    features: PredictionFeatures
    target: PredictionTarget


class PredictionRequest(BaseModel):
    model_name: str = Field(
        ..., example="RandomForest", description="Name of the prediction model to use."
    )
    features: List[PredictionFeatures] = Field(
        ..., description="List of predictions to make."
    )


class PredictionBatchInfo(BaseModel):
    id: int
    model_name: str
    predictions: List[PredictionInfo]
    timestamp: datetime = Field(
        default_factory=get_now(), description="Timestamp of the prediction batch."
    )
    cost: int = Field(..., description="Total cost of this batch of predictions.")


class PredictionsReport(BaseModel):
    model_name: str = Field(..., description="Name of the prediction model.")
    total_prediction_batches: int = Field(
        ..., description="Total number of prediction batches made using this model."
    )
