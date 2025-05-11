from pathlib import Path
from typing import Dict, List

import dill
import joblib

from core.repositories.predictor_repository import PredictorRepository


def load_model(model_name):
    # Грузим 3 модели
    model_names = {
        "LogisticRegression": "ml_models/catboost.dill",
        "SVM": "ml_models/svm.dill",
        "Catboost": "models/catboost.dill",
    }
    model_file = model_names[model_name]
    # Подстраивает корректный путь для загруженных моделей
    current_file_path = Path(__file__).resolve()
    project_root = current_file_path.parents[2]
    models_directory = project_root / "ml/ml_models"
    full_model_path = models_directory / model_file

    if not full_model_path.exists():
        raise FileNotFoundError(f"Model file not found at {full_model_path}")
    return joblib.load(full_model_path)


def load_pipeline():
    # грузит пайплайн и также подгоняет путь
    current_file_path = Path(__file__).resolve()
    project_root = current_file_path.parents[2]
    models_directory = project_root / "ml/ml_models"

    with open(models_directory / "preprocessing_pipeline.dill", "rb") as f:
        return dill.load(f)


class PredictorService:
    def __init__(self, predictor_repository: PredictorRepository):
        self.predictor_repository = predictor_repository

    def init_predictors(self):
        predictors = self.predictor_repository.get_all_predictors()
        if len(predictors) == 0:
            # Если нет предикторов, то добавляем logreg, svm, catboost
            self.predictor_repository.create_predictor(
                {"name": "LogisticRegression", "cost": 100}
            )
            self.predictor_repository.create_predictor({"name": "SVM", "cost": 250})
            self.predictor_repository.create_predictor(
                {"name": "Catboost", "cost": 500}
            )
        return self.predictor_repository.get_all_predictors()

    def get_available_models(self) -> List[Dict[str, str]]:
        # Получаем доступные модели предсказательные модели
        available_models = []
        predictors = self.predictor_repository.get_all_predictors()
        for predictor in predictors:
            available_models.append({"name": predictor.name, "cost": predictor.cost})
        return available_models

    def get_model_cost(self, model_name: str) -> int:
        # Получаем поле цена у предиктивной модели
        predictor = self.predictor_repository.get_predictor_by_name(model_name)
        if predictor:
            return predictor.cost
        raise ValueError(f"Model {model_name} is not available.")
