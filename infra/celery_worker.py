import os

from celery import Celery

from config.settings import settings

celery = Celery("prediction_worker")

celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", settings.BROKER_URL)
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", settings.BROKER_RESULT_BACKEND
)

celery.conf.update(
    task_serializer="pickle",
    result_serializer="pickle",
    accept_content=["pickle"],
    worker_send_task_events=True,
    worker_disable_rate_limits=False,
)


@celery.task
def async_make_batch_predictions(model_name, prediction_requests):
    import json
    from io import StringIO

    import pandas as pd

    from service.prediction_service import make_prediction
    from service.predictor_service import load_model

    model = load_model(model_name)
    # pipeline = load_pipeline()

    results = []

    df = pd.read_json(StringIO(json.dumps(prediction_requests)))

    results = make_prediction(model, df)

    return results
