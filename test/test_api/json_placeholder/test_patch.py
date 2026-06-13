import requests
from utils.api_config import JSON_BASE

URL = f"{JSON_BASE}/posts/1"

PATCH_PAYLOAD = {"title": "Título actualizado por PATCH"}

def test_patch_post():
    r = requests.patch(URL, json=PATCH_PAYLOAD)

    assert r.status_code == 200
    data = r.json()

    assert data["title"] == PATCH_PAYLOAD["title"]
