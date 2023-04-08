from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class TrainingData():
    __tablename__ = 'training_data'

    x = Column("x", Float, primary_key=True)
    y1 = Column("y1", Float, nullable=False)
    y2 = Column("y2", Float, nullable=False)
    y3 = Column("y3", Float, nullable=False)
    y4 = Column("y4", Float, nullable=False)

    def __init__(self, dataFrame):
        self.x = dataFrame.iloc[:, 0]
        self.y1 = dataFrame.iloc[:, 1]
        self.y2 = dataFrame.iloc[:, 2]
        self.y3 = dataFrame.iloc[:, 3]
        self.y4 = dataFrame.iloc[:, 4]

    def execute_sql(self):
        engine = create_engine('sqlite:///mydb.db', echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for i in range(len(self.x)):
            session.add(TrainingData(self.x[i], self.y1[i], self.y2[i], self.y3[i], self.y4[i]))

        session.commit()
        session.close()
