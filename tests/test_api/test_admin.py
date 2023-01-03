from routers.admin_end import admin as ad
from fastapi.testclient import TestClient

admin_client = TestClient(ad)


def test_admin_create(admin):
    new_admin_payload = admin.to_dict()

    admin_create_response = admin_client.post(
        url="/api/v1/admin", json=new_admin_payload
    )

    assert admin_create_response.status_code == 202
    assert admin_create_response.json()["username"] == "Kwabena"
    assert admin_create_response.json()["is_admin"] == True


def test_read_admin_details(admin):
    new_admin_payload = admin.to_dict()

    admin_create_response = admin_client.post("/api/v1/admin", json=new_admin_payload)

    # always check that a new admin has been created
    assert admin_create_response.status_code == 202

    old_admin_dat_response = admin_client.get(url="/api/v1/admin/1")
    assert old_admin_dat_response.status_code == 202
    assert old_admin_dat_response.json()
