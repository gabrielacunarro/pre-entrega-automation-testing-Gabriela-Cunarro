import requests
from utils.api_config import API_KEY, REQRES_BASE

headers = {"x-api-key": API_KEY}

def test_get_user_not_found():
    url = f"{REQRES_BASE}/users/99999"
    r = requests.get(url, headers=headers)

    assert r.status_code == 404
