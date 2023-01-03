from routers.user_end import user as usr
from fastapi.testclient import TestClient

client = TestClient(usr)


def test_create_user(user):
    new_user_payload = user.to_dict()

    user_create_response = client.post(url="/api/v1/user", json=new_user_payload)

    assert user_create_response.status_code == 200
    assert user_create_response.json()
    assert user_create_response.json()["is_admin"] == False

def test_read_user_details(user):
    new_user_payload = user.to_dict()
    create_user = client.post(url="/api/v1/user", json=new_user_payload)
    
    # assert if the user has been created first before we read from user_data
    assert create_user.status_code == 202

    old_user_dat_response = client.get(url="/api/v1/user/1")

    assert old_user_dat_response.status_code == 200
    assert old_user_dat_response.json()["username"] == "Prince"
    assert old_user_dat_response.json()["is_deleted"] == False
    