from sqlmodel import create_engine, SQLModel, Session

sqlite_url = "sqlite:///./dev.db"
engine = create_engine(sqlite_url, echo=False)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)
