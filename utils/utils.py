from sqlalchemy.orm import Session
from rps_remote_simulator.database.core import engine
from rps_remote_simulator.database.models import Base


def get_db():
    with Session(engine) as session:
        Base.metadata.create_all(bind=engine)
        yield session
