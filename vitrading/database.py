from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from vitrading.config import settings

engine = create_engine(settings.db.driver, echo=True)
SessionMaker = sessionmaker(bind=engine)
