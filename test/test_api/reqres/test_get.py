import requests
from utils.api_config import API_KEY, REQRES_BASE

headers = {"x-api-key": API_KEY}

def test_get_users_ok():
    url = f"{REQRES_BASE}/users?page=1"
    r = requests.get(url, headers=headers)

    assert r.status_code == 200
    data = r.json()

    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
