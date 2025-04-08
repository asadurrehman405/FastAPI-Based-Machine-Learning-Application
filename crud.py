from sqlalchemy.orm import Session
from model import Prediction
from schemas import LoanData

def create_prediction(db: Session, loan: LoanData, prediction: int):
    db_pred = Prediction(**loan.dict(), prediction=prediction)
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)
    return db_pred

def get_predictions(db: Session):
    return db.query(Prediction).all()
