from routers.user_end import user
from fastapi.testclient import TestClient

client = TestClient(user)


def test_create_user(user):
    new_user_payload = user.to_dict()

    response = client.post(url="/api/v1/user", json=new_user_payload)

    assert response.status_code == 200
    assert response.json()

def test_read_user_details():
    old_user_dat_response = client.get(url="/api/v1/user/1")

    assert old_user_dat_response.status_code == 200
    assert old_user_dat_response.json()["username"] == "Prince"
    assert old_user_dat_response.json()["is_deleted"] == False
    