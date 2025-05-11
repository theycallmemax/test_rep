from sqlalchemy import ForeignKey, Integer
from sqlmodel import Column, Field, Relationship, SQLModel


class Prediction(SQLModel, table=True):
    app_id: int = Field(primary_key=True)
    amnt: float = Field()
    currency: int = Field()
    operation_kind: int = Field()
    card_type: int = Field()
    operation_type: int = Field()
    operation_type_group: int = Field()
    ecommerce_flag: int = Field()
    payment_system: int = Field()
    income_flag: int = Field()
    mcc: int = Field()
    country: int = Field()
    city: int = Field()
    mcc_category: int = Field()
    day_of_week: int = Field()
    hour: int = Field()
    days_before: int = Field()
    weekofyear: int = Field()
    hour_diff: int = Field()
    transaction_number: int = Field()
    product: int = Field()
    batch_id: int = Field(sa_column=Column(Integer, ForeignKey("predictionbatch.id")))
    batch: "PredictionBatch" = Relationship(back_populates="predictions")
