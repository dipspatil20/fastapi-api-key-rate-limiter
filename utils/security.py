import secrets


def generate_api_key():
    # Generates a secure random 64-character API key
    return secrets.token_hex(32)