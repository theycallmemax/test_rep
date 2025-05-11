from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from core.entities.auth_schema import Payload
from core.entities.billing_schema import CreditsReport
from core.entities.prediction_schema import PredictionsReport
from core.entities.user_schema import UsersReport
from infra.container import Container
from infra.dependencies import get_current_superuser_payload
from service.billing_service import BillingService
from service.prediction_service import PredictionService
from service.user_service import UserService

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


@router.get("/users-report", response_model=UsersReport)
@inject
async def get_users_report(
    _: Payload = Depends(get_current_superuser_payload),
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    users_report = user_service.get_users_report()
    return users_report


@router.get("/predictions-reports", response_model=List[PredictionsReport])
@inject
async def get_predictions_report(
    _: Payload = Depends(get_current_superuser_payload),
    prediction_service: PredictionService = Depends(
        Provide[Container.prediction_service]
    ),
):
    predictions_reports = prediction_service.get_predictions_reports()
    return predictions_reports


@router.get("/credits-report", response_model=CreditsReport)
@inject
async def get_credits_report(
    _: Payload = Depends(get_current_superuser_payload),
    billing_service: BillingService = Depends(Provide[Container.billing_service]),
):
    credits_report = billing_service.get_credits_report()
    return credits_report
