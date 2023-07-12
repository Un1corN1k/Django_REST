import jwt
from datetime import datetime, timedelta


def generate_token():
    start_time = datetime.utcnow()
    expiry_time = start_time + timedelta(minutes=10)

    payload = {
        'sub': 'sasha',
        'iat': start_time,
        'exp': expiry_time,
    }

    secret_key = 'secret_key'
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token


new_token = generate_token()
print(new_token)
