from sqlalchemy import Column, Integer, Float
from database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Gender = Column(Integer)
    Married = Column(Integer)
    Dependents = Column(Float)
    Education = Column(Integer)
    Self_Employed = Column(Integer)
    ApplicantIncome = Column(Float)
    CoapplicantIncome = Column(Float)
    LoanAmount = Column(Float)
    Loan_Amount_Term = Column(Float)
    Credit_History = Column(Float)
    Property_Area_Semiurban = Column(Integer)
    Property_Area_Urban = Column(Integer)
    prediction = Column(Integer)
