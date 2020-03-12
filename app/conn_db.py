from sqlalchemy import create_engine

def get_conn():
    db_string = "postgresql://postgres:test123@localhost:5432/Alchemy"
    db = create_engine(db_string)
    return db
