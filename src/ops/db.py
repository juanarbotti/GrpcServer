# Sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_name = "data/users_database.sqlite3"

engine = create_engine(
    f'sqlite:///{db_name}',
    pool_pre_ping=True,
    pool_recycle=60
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()