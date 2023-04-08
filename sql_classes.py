from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DataSet():

    def __init__(self, dataFrame, tableName):
        self.dataFrame = dataFrame
        self.tableName = tableName

    def execute_sql(self):
        engine = create_engine('sqlite:///mydb.db', echo=True)
        Base.metadata.create_all(engine)

        self.dataFrame.to_sql(self.tableName, con=engine, if_exists='replace', index=False)
