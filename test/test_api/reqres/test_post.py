import requests
from utils.api_config import API_KEY, REQRES_BASE

headers = {"x-api-key": API_KEY}

def test_create_user_ok():
    url = f"{REQRES_BASE}/users"
    payload = {"name": "gabiii", "job": "tester"}

    r = requests.post(url, headers=headers, json=payload)

    assert r.status_code == 201
    data = r.json()

    assert "id" in data
    assert "createdAt" in data
