import os

import requests

API_URL = os.environ.get("API_URL", "http://localhost:8000/api")


class APIClient:
    def __init__(self, base_url=API_URL):
        self.base_url = base_url

    def _send_request(self, method, path, token=None, **kwargs):
        headers = kwargs.get("headers", {})
        if token:
            headers["Authorization"] = f"Bearer {token}"
        response = requests.request(
            method, f"{self.base_url}{path}", headers=headers, **kwargs
        )
        response.raise_for_status()
        return response.json()

    def get(self, path, token=None, **kwargs):
        return self._send_request("GET", path, token=token, **kwargs)

    def post(self, path, token=None, **kwargs):
        return self._send_request("POST", path, token=token, **kwargs)


api_client = APIClient()


def fetch_users_report(user_session):
    return api_client.get("/admin/users-report", token=user_session["access_token"])


def fetch_predictions_reports(user_session):
    return api_client.get(
        "/admin/predictions-reports", token=user_session["access_token"]
    )


def fetch_credits_report(user_session):
    return api_client.get("/admin/credits-report", token=user_session["access_token"])


def fetch_user_balance(user_session):
    response = api_client.get("/billing/balance", token=user_session["access_token"])
    return response


def deposit_amount(amount, user_session):
    response = api_client.post(
        "/billing/deposit",
        token=user_session["access_token"],
        json={"amount": amount},
    )
    return response


def fetch_transaction_history(user_session):
    response = api_client.get("/billing/history", token=user_session["access_token"])
    return response


def fetch_models(user_session):
    response = api_client.get("/prediction/models", token=user_session["access_token"])
    return response


def fetch_prediction_history(user_session):
    response = api_client.get("/prediction/history", token=user_session["access_token"])
    return response


def send_prediction_request(selected_model, json, user_session):
    payload = {"model_name": selected_model, "features": json}
    response = api_client.post(
        "/prediction/make", json=payload, token=user_session["access_token"]
    )
    return response


def authenticate_user(email, password):
    try:
        response = api_client.post(
            "/auth/sign-in", json={"email": email, "password": password}
        )
        if response:
            return response, None
        else:
            return None, "Authentification failed: No response from server"
    except Exception as e:
        return None, str(e)


def register_user(email, password, name):
    try:
        response = api_client.post(
            "/auth/sign-up",
            json={"email": email, "password": password, "name": name},
        )
        if response:
            return response, None
        else:
            return None, "Registration failed: No response from server"
    except Exception as e:
        return None, str(e)
