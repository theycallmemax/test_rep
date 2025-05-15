def authentificated_session(user_data):
    """
    Creates a session object from user data returned by the API
    """
    return {
        "id": user_data.get("id"),
        "email": user_data.get("email"),
        "name": user_data.get("name"),
        "is_superuser": user_data.get("is_superuser", False),
        "is_authenticated": True,
        "access_token": user_data.get("access_token"),
    }