import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    payload = {"title": "Aprendendo API", "body": "Dia 1 com Python!", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data.get("title") == payload["title"]

def test_list_users():
    r = requests.get(f"{BASE_URL}/users")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 10

def test_user_5():
    r = requests.get(f"{BASE_URL}/users/5")
    assert r.status_code == 200
    data = r.json()
    assert data.get("name") == "Chelsey Dietrich"
