import logging
import db_config
from logging.config import dictConfig
from projutil.log_conf import DIC_LOGGING_CONFIG
from projutil.conf import LOGGER_NAME
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from PySide6.QtSql import QSqlDatabase
from db.tables import create_tables, KeyStore, create_orders_view
from sqlalchemy import update
from datetime import datetime
from db.db_config import DATABASE_CONNECTION_NAME


dictConfig(DIC_LOGGING_CONFIG)
logger = logging.getLogger(LOGGER_NAME)


class DB:
    db = None
    engine = create_engine(
        f"sqlite:///{db_config.DATABASE_NAME}", echo=True, future=True)

    def __init__(self):
        create_tables(engine=self.engine)
        create_orders_view(engine=self.engine)
        self.session = Session(self.engine)
        self.initialize_qsql()

    def get_session(self):
        return self.session

    def initialize_qsql(self):
        self.db = QSqlDatabase.addDatabase(
            "QSQLITE", connectionName=db_config.DATABASE_CONNECTION_NAME)
        self.db.setDatabaseName(db_config.DATABASE_NAME)
        if self.db.open():
            print("Database opened in QT")
        # self.ready_tables()

    def insert_into_keystore(self, key, value):
        if value == "":
            return
        kv = KeyStore(key=key, value=value)
        self.session.add(kv)
        self.session.commit()
        return kv

    def get_value_from_key(self, key):
        key_value = (self.session.query(KeyStore)
                     .filter_by(key=key)
                     .first()
                     )
        return key_value

    def update_key_vlue(self, key, value):
        stmt = (
            update(KeyStore)
            .filter(KeyStore.key == key)
            .values(value=value)
        )
        self.session.execute(stmt)
        self.session.commit()

    def close(self):
        self.session.close()


if __name__ == "__main__":
    db = DB()
