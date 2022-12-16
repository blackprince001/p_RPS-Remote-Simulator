from schemas.user import UserCreate, AdminCreate
from datetime import datetime

time = datetime.now()

def test_user_dataclass():
    user = UserCreate(username="Prince", date_created=time)

    assert user.username == "Prince"
    assert user.username != "Kwabena"
    assert user.date_created


def test_admin_dataclass():
    admin = AdminCreate(username="Prince", date_created=time)

    assert admin.username == "Kwabena"
    assert admin.is_admin is True
    assert admin.date_created
