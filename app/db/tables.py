from db import db_config
from sqlalchemy import Column
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy import Integer, Boolean, Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class KeyStore(Base):
    __tablename__ = db_config.TABLE_NAME_KEYSTORE
    key = Column(String, primary_key=True)
    value = Column(String)

def create_tables(engine):
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()

    # d = [column.info.get('verbose_name')
    #      for column in Formulation.__table__.columns]
    # print(d)
