from pydantic import BaseModel

class LoanData(BaseModel):
    Gender: int
    Married: int
    Dependents: float
    Education: int
    Self_Employed: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area_Semiurban: int
    Property_Area_Urban: int

class PredictionOut(BaseModel):
    id: int
    prediction: int

class PredictionInDB(LoanData):
    prediction: int
