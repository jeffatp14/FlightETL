from module.log import get_logger
from module.job import sink_config
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import extras


logging = get_logger()

class Postgres:
    def __init__(self):
        self.config = sink_config
        self.connection = None
        self.engine = None
        self.connection_string = None
        self.cursor = None
        self.connected()

    def connected(self):
        self.connection_string = f"postgresql+psycopg2://{self.config['username']}:{self.config['password']}@{self.config['host']}:{self.config['port']}/{self.config['database']}"

        # SQLAlchemy engine
        self.engine = create_engine(self.connection_string)

        # psycopg2 connection
        self.connection = psycopg2.connect(
            host=self.config['host'],
            database=self.config['database'],
            user=self.config['username'],
            password=self.config['password'],
            port=self.config['port']
        )

        logging.info("CLIENT - PostgreSQL connection established.")

    def get_engine(self):
        # just return the engine object, do NOT call it
        return self.engine

    def close_connection(self):
        if self.connection:
            self.connection.close()
