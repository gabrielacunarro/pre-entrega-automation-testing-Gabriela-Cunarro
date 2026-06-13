import requests
from utils.api_config import JSON_BASE

URL = f"{JSON_BASE}/posts/1"

def test_delete_post():
    r = requests.delete(URL)

    assert r.status_code == 200 or r.status_code == 204
