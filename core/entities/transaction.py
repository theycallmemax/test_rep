from entities.base_model import BaseModel
from sqlmodel import Field, Relationship


class Transaction(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id")
    amount: int = Field()
    prediction_batch: "PredictionBatch" = Relationship(back_populates="transaction")
