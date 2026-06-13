import requests
from utils.api_config import API_KEY, REQRES_BASE

headers = {"x-api-key": API_KEY}

def test_delete_user_ok():
    url = f"{REQRES_BASE}/users/2"
    r = requests.delete(url, headers=headers)

    assert r.status_code == 204
    assert r.text == ""
