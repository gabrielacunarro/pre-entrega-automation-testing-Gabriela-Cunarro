import requests
from utils.api_config import JSON_BASE

URL = f"{JSON_BASE}/posts/1"

payload = {
    "id": 1,
    "title": "Automation Testing Guide",
    "body": "Guía completa de testing automatizado",
    "userId": 1
}

def test_put_post():
    r = requests.put(URL, json=payload)

    assert r.status_code == 200
    data = r.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["id"] == 1
